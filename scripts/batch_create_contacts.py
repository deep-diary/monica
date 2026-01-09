"""
批量创建联系人脚本
从 contacts.csv 读取数据并批量创建联系人，同时创建/更新地址、邮箱和电话

使用方法:
    1. 确保已安装依赖: pip install pypinyin
    2. 配置环境变量（可选）:
       - MONICA_TOKEN: Monica API token
       - MONICA_BASE_URL: Monica API 基础 URL
    3. 运行脚本: python batch_create_contacts.py

依赖:
    - pypinyin: 用于中文转拼音（ContactManager.generate_nickname 需要）
    - aiohttp: 用于异步 HTTP 请求（pymonica 已包含）

CSV 文件格式:
    FirstName, LastName, NickName, Gender, Email, Phone, Address, City, Resource, Need
"""

import csv
import sys
import os
import asyncio

# 添加父目录到路径，以便导入 pymonica 包
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pymonica import MonicaClient
from pymonica.contact_manager import ContactManager


def find_contact_id(first_name: str, last_name: str, nickname: str, contacts_data: list) -> str:
    """
    在联系人列表中查找联系人 ID
    
    Args:
        first_name: 名字
        last_name: 姓氏
        nickname: 昵称
        contacts_data: 现有联系人列表
    
    Returns:
        联系人 ID，如果找不到则返回 None
    """
    # 构建期望的姓名（格式：last_name + first_name，去除空格）
    expected_name1 = f"{last_name}{first_name}".strip().replace(' ', '')
    expected_name2 = f"{first_name}{last_name}".strip().replace(' ', '')
    expected_nickname = nickname.strip('[]').replace(' ', '').lower() if nickname else None
    
    for contact in contacts_data:
        contact_id = contact.get('id')
        if not contact_id:
            continue
        
        # 检查姓名匹配
        contact_name = contact.get('name', '').strip().replace(' ', '')
        contact_first_name = contact.get('first_name', '').strip()
        contact_last_name = contact.get('last_name', '').strip()
        
        # 构建联系人的姓名格式
        contact_name_format1 = f"{contact_last_name}{contact_first_name}".replace(' ', '') if contact_first_name and contact_last_name else ''
        contact_name_format2 = f"{contact_first_name}{contact_last_name}".replace(' ', '') if contact_first_name and contact_last_name else ''
        
        # 检查姓名匹配
        if (contact_name == expected_name1 or contact_name == expected_name2 or
            contact_name_format1 == expected_name1 or contact_name_format1 == expected_name2 or
            contact_name_format2 == expected_name1 or contact_name_format2 == expected_name2):
            return contact_id
        
        # 检查昵称匹配
        if expected_nickname:
            contact_nickname = contact.get('nickname', '').strip().strip('[]').replace(' ', '').lower()
            if contact_nickname == expected_nickname:
                return contact_id
    
    return None


async def sync_contact_info(client, vault_id: str, contact_id: str, email: str = None, 
                           phone: str = None, verbose: bool = False):
    """
    同步联系人的邮箱和电话信息
    
    Args:
        client: MonicaClient 实例
        vault_id: Vault ID
        contact_id: 联系人 ID
        email: 邮箱地址（可选）
        phone: 电话号码（可选）
        verbose: 是否打印详细信息
    """
    # 获取联系人详情以检查现有信息
    contact_detail = await client.contacts.get(vault_id, contact_id)
    
    # 提取现有的联系信息
    existing_emails = []
    existing_phones = []
    
    if contact_detail:
        # 尝试从 HTML 解析的数据中提取联系信息
        # 注意：这取决于 Monica API 返回的数据结构
        props = contact_detail.get('props', {})
        contact_data = props.get('data', {})
        contact_info_list = contact_data.get('contactInformation', [])
        
        for info in contact_info_list:
            info_type = info.get('contact_information_type', {})
            info_type_id = info_type.get('id')
            info_data = info.get('data', '')
            info_id = info.get('id')
            
            if info_type_id == 1:  # 邮箱
                existing_emails.append({'id': info_id, 'data': info_data})
            elif info_type_id == 2:  # 电话
                existing_phones.append({'id': info_id, 'data': info_data})
    
    # 处理邮箱
    if email:
        email = email.strip()
        if email:
            # 检查是否已存在相同的邮箱
            email_exists = False
            email_id = None
            
            for existing_email in existing_emails:
                if existing_email.get('data', '').lower() == email.lower():
                    email_exists = True
                    email_id = existing_email.get('id')
                    break
            
            if email_exists and email_id:
                # 更新现有邮箱
                if verbose:
                    print(f"    更新邮箱: {email}")
                await client.contact_information.update_email(vault_id, contact_id, str(email_id), email)
            else:
                # 创建新邮箱
                if verbose:
                    print(f"    创建邮箱: {email}")
                await client.contact_information.create_email(vault_id, contact_id, email)
    
    # 处理电话
    if phone:
        phone = phone.strip()
        if phone:
            # 检查是否已存在相同的电话
            phone_exists = False
            phone_id = None
            
            for existing_phone in existing_phones:
                if existing_phone.get('data', '') == phone:
                    phone_exists = True
                    phone_id = existing_phone.get('id')
                    break
            
            if phone_exists and phone_id:
                # 更新现有电话
                if verbose:
                    print(f"    更新电话: {phone}")
                await client.contact_information.update_phone(vault_id, contact_id, str(phone_id), phone)
            else:
                # 创建新电话
                if verbose:
                    print(f"    创建电话: {phone}")
                await client.contact_information.create_phone(vault_id, contact_id, phone)


async def sync_contact_address(client, vault_id: str, contact_id: str, address: str = None, 
                              city: str = None, verbose: bool = False):
    """
    同步联系人的地址信息
    
    Args:
        client: MonicaClient 实例
        vault_id: Vault ID
        contact_id: 联系人 ID
        address: 地址（可选）
        city: 城市（可选）
        verbose: 是否打印详细信息
    """
    if not address or not city:
        return
    
    address = address.strip()
    city = city.strip()
    
    if not address or not city:
        return
    
    # 创建地址（工作地址）
    if verbose:
        print(f"    创建地址: {address}, {city}")
    
    # 默认使用工作地址类型，如果没有省份信息，使用默认值
    await client.addresses.create(
        vault_id=vault_id,
        contact_id=contact_id,
        line_1=address,
        city=city,
        province="",  # CSV 中没有省份信息，使用空字符串
        country="中国",  # 默认国家
        address_type_id=client.addresses.ADDRESS_TYPE_WORK  # 工作地址
    )


async def batch_create_contacts(csv_file: str, monica_token: str, monica_base_url: str, vault_id: str):
    """
    批量创建/更新联系人及其相关信息（地址、邮箱、电话）
    
    Args:
        csv_file: CSV 文件路径
        monica_token: Monica API token
        monica_base_url: Monica API 基础 URL
        vault_id: Vault ID
    """
    # 读取 CSV 文件
    contacts_to_create = []
    
    try:
        with open(csv_file, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            
            # 辅助函数：尝试多个可能的列名
            def get_field(row, possible_names):
                for name in possible_names:
                    value = row.get(name, '')
                    if value:
                        return value.strip()
                return ''
            
            for row in reader:
                # 尝试多种可能的列名（处理列名中可能存在的空格）
                first_name = get_field(row, ['FirstName', 'First Name', 'first_name', 'first name'])
                last_name = get_field(row, ['LastName', 'Last Name', 'last_name', 'last name'])
                gender = get_field(row, ['Gender', 'gender', ' Gender', 'Gender '])
                email = get_field(row, ['Email', 'email', 'Email '])
                phone = get_field(row, ['Phone', 'phone', 'Phone '])
                address = get_field(row, ['Address', 'address', 'Address '])
                city = get_field(row, ['City', 'city', 'City '])
                
                # 跳过空行
                if not first_name and not last_name:
                    continue
                
                # 生成昵称（使用 ContactManager 的静态方法）
                try:
                    nickname = ContactManager.generate_nickname(last_name, first_name)
                except ImportError as e:
                    print(f"错误: {e}")
                    sys.exit(1)
                
                # 映射性别（使用 ContactManager 的静态方法）
                gender_id = ContactManager.map_gender(gender)
                
                contacts_to_create.append({
                    'first_name': first_name,
                    'last_name': last_name,
                    'nickname': nickname,
                    'gender_id': gender_id,
                    'gender_str': gender,  # 保留原始性别字符串用于显示
                    'email': email,
                    'phone': phone,
                    'address': address,
                    'city': city
                })
    except FileNotFoundError:
        print(f"错误: 找不到文件 {csv_file}")
        return
    except Exception as e:
        print(f"错误: 读取 CSV 文件失败: {e}")
        return
    
    if not contacts_to_create:
        print("警告: CSV 文件中没有有效的联系人数据")
        return
    
    # 创建客户端并批量创建/更新联系人
    async with MonicaClient(monica_token, monica_base_url) as client:
        # 先获取所有现有联系人
        print("正在获取现有联系人列表...")
        existing_contacts = await client.contacts.list_all(vault_id=vault_id, verbose=False)
        print(f"已获取 {len(existing_contacts)} 个现有联系人\n")
        
        # 使用 ContactManager 的批量创建/更新方法
        print("=" * 50)
        print("批量创建/更新联系人")
        print("=" * 50)
        stats = await client.contacts.batch_create_or_update(
            vault_id=vault_id,
            contacts_data=contacts_to_create,
            verbose=True,
            debug=False
        )
        
        # 重新获取联系人列表（包含新创建的）
        print("\n正在重新获取联系人列表...")
        all_contacts = await client.contacts.list_all(vault_id=vault_id, verbose=False)
        
        # 为每个联系人同步地址、邮箱和电话
        print("\n" + "=" * 50)
        print("同步联系人详细信息（地址、邮箱、电话）")
        print("=" * 50)
        
        for i, contact_data in enumerate(contacts_to_create, 1):
            first_name = contact_data['first_name']
            last_name = contact_data['last_name']
            nickname = contact_data['nickname']
            email = contact_data.get('email', '')
            phone = contact_data.get('phone', '')
            address = contact_data.get('address', '')
            city = contact_data.get('city', '')
            
            print(f"\n[{i}/{len(contacts_to_create)}] 处理联系人: {last_name}{first_name}")
            
            # 查找联系人 ID（batch_create_or_update 已经创建/更新了联系人）
            contact_id = find_contact_id(first_name, last_name, nickname, all_contacts)
            
            if not contact_id:
                print(f"  ✗ 无法找到联系人 ID（可能创建失败）")
                continue
            
            # 同步联系信息（邮箱和电话）
            await sync_contact_info(
                client, vault_id, contact_id, email, phone, verbose=True
            )
            
            # 同步地址信息
            await sync_contact_address(
                client, vault_id, contact_id, address, city, verbose=True
            )
        
        print("\n" + "=" * 50)
        print("批量处理完成！")
        print(f"  新建: {stats['created']} 个")
        print(f"  更新: {stats['updated']} 个")
        print(f"  失败: {stats['failed']} 个")
        print(f"  总计: {stats['total']} 个")
        print("=" * 50)


async def main():
    """主函数"""
    # 配置信息
    # 可以从环境变量或配置文件读取
    monica_token = os.getenv("MONICA_TOKEN", "8m3ihVnLHt8B7QeuWn7GJdDCKEqwNoe7hVKtSugZ576f1c46")  # 默认值，建议使用环境变量
    monica_base_url = os.getenv("MONICA_BASE_URL", "http://mem.deep-diary.com")  # 默认值
    # vault_id = "019b83ae-f4bc-7360-bab1-84e226a00e43"  # friends vault
    vault_id = "019b83b0-bd96-700c-bb9a-9bd74f99202f" # colleagues vault
    
    # CSV 文件路径（相对于脚本目录）
    script_dir = os.path.dirname(os.path.abspath(__file__))
    csv_file = os.path.join(script_dir, "colleagues.csv")
    
    # 执行批量创建
    await batch_create_contacts(csv_file, monica_token, monica_base_url, vault_id)


if __name__ == "__main__":
    asyncio.run(main())


"""
批量创建联系人脚本
从 contacts.csv 读取数据并批量创建联系人

使用方法:
    1. 确保已安装依赖: pip install pypinyin
    2. 配置环境变量（可选）:
       - MONICA_TOKEN: Monica API token
       - MONICA_BASE_URL: Monica API 基础 URL
    3. 运行脚本: python batch_create_contacts.py

依赖:
    - pypinyin: 用于中文转拼音
    - aiohttp: 用于异步 HTTP 请求（pymonica 已包含）
"""

import csv
import sys
import os
import asyncio

try:
    from pypinyin import lazy_pinyin, Style
except ImportError:
    print("错误: 未安装 pypinyin 库")
    print("请运行: pip install pypinyin")
    sys.exit(1)

# 添加父目录到路径，以便导入 pymonica 包
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pymonica import MonicaClient


def generate_nickname(last_name: str, first_name: str) -> str:
    """
    使用 pypinyin 将中文姓名转换为全拼，格式为全小写无空格（便于检索）
    
    Args:
        last_name: 姓氏
        first_name: 名字
    
    Returns:
        格式化的昵称，例如: machengxue
    """
    # 将中文转换为拼音（全拼，不带声调）
    last_name_pinyin = ''.join(lazy_pinyin(last_name, style=Style.NORMAL))
    first_name_pinyin = ''.join(lazy_pinyin(first_name, style=Style.NORMAL))
    
    # 格式化为全小写无空格（便于检索）
    return f"{last_name_pinyin}{first_name_pinyin}".lower()


def map_gender(gender_str: str) -> str:
    """
    将性别字符串映射到 gender_id
    
    Args:
        gender_str: 性别字符串，如 "男"、"女" 等
    
    Returns:
        gender_id 字符串，如 "1"、"2" 等
    """
    gender_map = {
        "男": "1",
        "女": "2",
        "male": "1",
        "female": "2",
        "m": "1",
        "f": "2",
    }
    
    # 去除空格并转换为小写进行比较
    gender_clean = gender_str.strip().lower() if isinstance(gender_str, str) else ""
    
    # 如果是中文，直接查找
    if gender_str.strip() in gender_map:
        return gender_map[gender_str.strip()]
    
    # 如果是英文，查找小写版本
    if gender_clean in gender_map:
        return gender_map[gender_clean]
    
    # 如果找不到匹配，返回空字符串（可选字段）
    return ""


async def get_all_contacts(client, vault_id: str) -> list:
    """
    获取 vault 中的所有联系人（处理分页）
    
    Args:
        client: MonicaClient 实例
        vault_id: Vault ID
    
    Returns:
        所有联系人的列表
    """
    all_contacts = []
    page = 1
    limit = 100  # 每页获取更多联系人以减少请求次数
    
    print("正在获取现有联系人列表...")
    
    while True:
        contacts_data = await client.contacts.list(vault_id=vault_id, limit=limit, page=page)
        
        if not contacts_data:
            break
        
        # 提取联系人列表
        contacts = client.contacts.extract_contacts_from_response(contacts_data)
        
        if not contacts:
            break
        
        all_contacts.extend(contacts)
        
        # 检查是否还有更多页面
        paginator = None
        if 'props' in contacts_data and 'data' in contacts_data['props']:
            paginator = contacts_data['props']['data'].get('paginator', {})
        elif 'data' in contacts_data:
            if isinstance(contacts_data['data'], dict):
                paginator = contacts_data['data'].get('paginator', {})
        
        if paginator:
            current_page = paginator.get('current_page', page)
            last_page = paginator.get('last_page', 1)
            if current_page >= last_page:
                break
        
        page += 1
    
    print(f"已获取 {len(all_contacts)} 个现有联系人")
    
    # 打印现有联系人详细信息（用于调试）
    if all_contacts:
        print("\n现有联系人列表:")
        import json
        for i, contact in enumerate(all_contacts, 1):
            contact_id = contact.get('id', 'N/A')
            contact_name = contact.get('name', 'N/A')
            contact_nickname = contact.get('nickname', 'N/A')
            # 打印所有可用字段
            print(f"  {i}. ID: {contact_id}")
            print(f"     姓名: {contact_name}")
            print(f"     昵称: {contact_nickname}")
            # 打印所有字段（用于调试）
            print(f"     所有字段: {list(contact.keys())}")
            # 如果有 first_name 和 last_name 字段，也打印出来
            if 'first_name' in contact:
                print(f"     first_name: {contact.get('first_name')}")
            if 'last_name' in contact:
                print(f"     last_name: {contact.get('last_name')}")
            print()
        print()
    
    return all_contacts


async def get_contact_details(client, vault_id: str, contact_id: str) -> dict:
    """
    获取联系人详细信息
    
    Args:
        client: MonicaClient 实例
        vault_id: Vault ID
        contact_id: 联系人 ID
    
    Returns:
        联系人详细信息字典
    """
    contact_detail = await client.contacts.get(vault_id, contact_id)
    
    if not contact_detail:
        return {}
    
    # 从响应中提取联系人数据
    contact_data = {}
    if 'props' in contact_detail and 'data' in contact_detail['props']:
        contact_data = contact_detail['props']['data']
    elif 'data' in contact_detail:
        contact_data = contact_detail['data']
    
    return contact_data


def find_existing_contact(contacts: list, first_name: str, last_name: str, nickname: str, debug: bool = False) -> dict:
    """
    在现有联系人列表中查找匹配的联系人
    
    匹配规则：
    1. 优先通过姓名匹配（first_name + last_name）
    2. 如果姓名匹配，则认为是同一个联系人
    3. 也可以通过昵称匹配
    
    Args:
        contacts: 现有联系人列表
        first_name: 名字
        last_name: 姓氏
        nickname: 昵称（用于显示和匹配）
        debug: 是否打印调试信息
    
    Returns:
        如果找到匹配的联系人，返回包含 contact_id 和 match_type 的字典；否则返回 None
    """
    # 构建期望的姓名（支持两种格式：last_name+first_name 和 first_name+last_name）
    expected_name1 = f"{last_name}{first_name}".strip()  # 格式1: 马成学
    expected_name2 = f"{first_name} {last_name}".strip()  # 格式2: 成学 马
    expected_name3 = f"{first_name}{last_name}".strip()  # 格式3: 成学马（无空格）
    
    # 去除空格后的版本（用于灵活匹配）
    expected_name_no_space = f"{last_name}{first_name}".replace(' ', '')
    expected_name_reverse_no_space = f"{first_name}{last_name}".replace(' ', '')
    
    if debug:
        print(f"    调试: 查找联系人 - 姓名格式1: {expected_name1}, 格式2: {expected_name2}, 昵称: {nickname}")
    
    for contact in contacts:
        contact_id = contact.get('id')
        if not contact_id:
            continue
        
        # 通过姓名匹配（Monica 中姓名可能是 first_name + 空格 + last_name 或 last_name + first_name）
        contact_name = contact.get('name', '').strip()
        contact_name_no_space = contact_name.replace(' ', '')  # 去除空格用于比较
        
        if debug:
            print(f"    调试: 比较 - 现有联系人: ID={contact_id}, 姓名='{contact_name}', 昵称='{contact.get('nickname', '')}'")
        
        # 精确匹配姓名（支持多种格式）
        if (contact_name == expected_name1 or 
            contact_name == expected_name2 or 
            contact_name == expected_name3 or
            contact_name_no_space == expected_name_no_space or
            contact_name_no_space == expected_name_reverse_no_space):
            if debug:
                print(f"    调试: ✓ 通过姓名匹配成功 (现有: '{contact_name}', 期望格式之一)")
            return {'contact_id': contact_id, 'match_type': 'name'}
        
        # 如果联系人列表中有 nickname 字段，也可以通过昵称匹配
        contact_nickname = contact.get('nickname', '').strip()
        if contact_nickname:
            # 去除昵称中的方括号、空格等格式字符进行比较
            # 处理旧格式 [Ma Chengxue] 和新格式 machengxue
            contact_nickname_clean = contact_nickname.strip('[]').replace(' ', '').lower()
            nickname_clean = nickname.strip('[]').replace(' ', '').lower()
            
            if debug:
                print(f"    调试: 昵称比较 - 现有: '{contact_nickname_clean}', 期望: '{nickname_clean}'")
            
            if contact_nickname_clean == nickname_clean:
                if debug:
                    print(f"    调试: ✓ 通过昵称匹配成功")
                return {'contact_id': contact_id, 'match_type': 'nickname'}
        
        # 如果联系人列表中有 first_name 和 last_name 字段，进行精确匹配
        contact_first_name = contact.get('first_name', '').strip()
        contact_last_name = contact.get('last_name', '').strip()
        if contact_first_name and contact_last_name:
            if contact_first_name == first_name and contact_last_name == last_name:
                if debug:
                    print(f"    调试: ✓ 通过 first_name/last_name 匹配成功")
                return {'contact_id': contact_id, 'match_type': 'first_last_name'}
    
    if debug:
        print(f"    调试: ✗ 未找到匹配的联系人")
    
    return None


async def batch_create_contacts(csv_file: str, monica_token: str, monica_base_url: str, vault_id: str):
    """
    批量创建/更新联系人
    
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
                
                # 跳过空行
                if not first_name and not last_name:
                    continue
                
                # 生成昵称（使用 pypinyin）
                nickname = generate_nickname(last_name, first_name)
                
                # 映射性别
                gender_id = map_gender(gender)
                
                contacts_to_create.append({
                    'first_name': first_name,
                    'last_name': last_name,
                    'nickname': nickname,
                    'gender_id': gender_id,
                    'gender_str': gender  # 保留原始性别字符串用于显示
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
    
    print(f"准备处理 {len(contacts_to_create)} 个联系人...")
    print()
    
    # 创建客户端并批量创建/更新联系人
    async with MonicaClient(monica_token, monica_base_url) as client:
        # 先获取所有现有联系人
        existing_contacts = await get_all_contacts(client, vault_id)
        print()
        
        create_count = 0
        update_count = 0
        fail_count = 0
        
        for i, contact_data in enumerate(contacts_to_create, 1):
            first_name = contact_data['first_name']
            last_name = contact_data['last_name']
            nickname = contact_data['nickname']
            gender_id = contact_data['gender_id']
            gender_str = contact_data['gender_str']
            
            print(f"[{i}/{len(contacts_to_create)}] 处理联系人: {last_name}{first_name} (昵称: {nickname}, 性别: {gender_str})")
            
            try:
                # 查找是否已存在（启用调试模式）
                existing = find_existing_contact(existing_contacts, first_name, last_name, nickname, debug=True)
                
                if existing:
                    # 联系人已存在，执行更新
                    contact_id = existing['contact_id']
                    match_type = existing['match_type']
                    print(f"  → 联系人已存在 (ID: {contact_id}, 匹配方式: {match_type})，执行更新...")
                    
                    result = await client.contacts.update(
                        vault_id=vault_id,
                        contact_id=contact_id,
                        first_name=first_name,
                        last_name=last_name,
                        nickname=nickname,
                        gender_id=gender_id if gender_id else ""
                    )
                    
                    if result:
                        update_count += 1
                        print(f"  ✓ 更新成功")
                    else:
                        fail_count += 1
                        print(f"  ✗ 更新失败: 未返回结果")
                else:
                    # 联系人不存在，执行创建
                    print(f"  → 联系人不存在，执行创建...")
                    
                    result = await client.contacts.create(
                        vault_id=vault_id,
                        first_name=first_name,
                        last_name=last_name,
                        nickname=nickname,
                        gender_id=gender_id if gender_id else ""
                    )
                    
                    if result:
                        create_count += 1
                        print(f"  ✓ 创建成功")
                        
                        # 如果创建成功，尝试从结果中提取联系人 ID 并添加到现有列表
                        # 这样可以避免 CSV 中重复行导致的重复创建
                        contact_url = result.get('data', '')
                        if contact_url and '/contacts/' in contact_url:
                            contact_id = contact_url.split('/contacts/')[-1].split('?')[0].split('#')[0]
                            if contact_id:
                                # 将新联系人添加到现有列表（简化版本，只包含必要字段）
                                existing_contacts.append({
                                    'id': contact_id,
                                    'name': f"{last_name}{first_name}",
                                    'nickname': nickname
                                })
                    else:
                        fail_count += 1
                        print(f"  ✗ 创建失败: 未返回结果")
                    
            except Exception as e:
                fail_count += 1
                print(f"  ✗ 操作失败: {e}")
            
            print()
        
        # 打印总结
        print("=" * 50)
        print(f"批量处理完成!")
        print(f"  新建: {create_count} 个")
        print(f"  更新: {update_count} 个")
        print(f"  失败: {fail_count} 个")
        print(f"  总计: {len(contacts_to_create)} 个")
        print("=" * 50)


async def main():
    """主函数"""
    # 配置信息
    # 可以从环境变量或配置文件读取
    monica_token = os.getenv("MONICA_TOKEN", "8m3ihVnLHt8B7QeuWn7GJdDCKEqwNoe7hVKtSugZ576f1c46")  # 默认值，建议使用环境变量
    monica_base_url = os.getenv("MONICA_BASE_URL", "http://mem.deep-diary.com")  # 默认值
    vault_id = "019b83ae-f4bc-7360-bab1-84e226a00e43"  # friends vault
    
    # CSV 文件路径（相对于脚本目录）
    script_dir = os.path.dirname(os.path.abspath(__file__))
    csv_file = os.path.join(script_dir, "contacts.csv")
    
    # 执行批量创建
    await batch_create_contacts(csv_file, monica_token, monica_base_url, vault_id)


if __name__ == "__main__":
    asyncio.run(main())


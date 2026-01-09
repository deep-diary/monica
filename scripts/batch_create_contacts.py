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
    - pypinyin: 用于中文转拼音（ContactManager.generate_nickname 需要）
    - aiohttp: 用于异步 HTTP 请求（pymonica 已包含）
"""

import csv
import sys
import os
import asyncio

# 添加父目录到路径，以便导入 pymonica 包
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pymonica import MonicaClient
from pymonica.contact_manager import ContactManager


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
    
    # 创建客户端并批量创建/更新联系人
    async with MonicaClient(monica_token, monica_base_url) as client:
        # 使用 ContactManager 的批量创建/更新方法
        stats = await client.contacts.batch_create_or_update(
            vault_id=vault_id,
            contacts_data=contacts_to_create,
            verbose=True,
            debug=True  # 启用调试模式以查看匹配过程
        )


async def main():
    """主函数"""
    # 配置信息
    # 可以从环境变量或配置文件读取
    monica_token = os.getenv("MONICA_TOKEN", "8m3ihVnLHt8B7QeuWn7GJdDCKEqwNoe7hVKtSugZ576f1c46")  # 默认值，建议使用环境变量
    monica_base_url = os.getenv("MONICA_BASE_URL", "http://192.168.31.25:8080")  # 默认值
    # vault_id = "019b83ae-f4bc-7360-bab1-84e226a00e43"  # friends vault
    vault_id = "019b83b0-bd96-700c-bb9a-9bd74f99202f" # colleagues vault
    
    # CSV 文件路径（相对于脚本目录）
    script_dir = os.path.dirname(os.path.abspath(__file__))
    csv_file = os.path.join(script_dir, "colleagues.csv")
    
    # 执行批量创建
    await batch_create_contacts(csv_file, monica_token, monica_base_url, vault_id)


if __name__ == "__main__":
    asyncio.run(main())


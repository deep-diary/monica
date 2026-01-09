"""
测试联系人信息（ContactInformation）功能
"""

import json
import sys
import os
import asyncio

# 添加父目录到路径，以便导入 pymonica 包
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pymonica import MonicaClient


async def main():
    # 配置信息
    monica_token = "8m3ihVnLHt8B7QeuWn7GJdDCKEqwNoe7hVKtSugZ576f1c46"
    monica_base_url = "http://mem.deep-diary.com"
    vault_id = "019ba163-d71f-70d0-b3cc-f8a53413f24b"
    contact_id = "019ba163-d7a3-72b5-96b5-ba4ea81c0406"
    
    # 创建客户端实例
    async with MonicaClient(monica_token, monica_base_url) as client:
        # 测试 1: 创建邮箱
        print("=" * 50)
        print("测试 1: 创建邮箱")
        print("=" * 50)
        
        email = "deep-diary@qq.com"
        print(f"邮箱: {email}")
        
        create_email_result = await client.contact_information.create_email(
            vault_id=vault_id,
            contact_id=contact_id,
            email=email
        )
        
        if create_email_result:
            print("\n创建邮箱成功:")
            print(json.dumps(create_email_result, indent=2, ensure_ascii=False))
            
            # 从响应中提取 contact_information_id
            contact_info_id = None
            if 'data' in create_email_result:
                data = create_email_result['data']
                if isinstance(data, dict):
                    contact_info_id = str(data.get('id', ''))
                    print(f"\n创建的联系人信息 ID: {contact_info_id}")
        else:
            print("创建邮箱失败")
        
        # 测试 2: 创建电话
        print("\n" + "=" * 50)
        print("测试 2: 创建电话")
        print("=" * 50)
        
        phone = "15055305685"
        print(f"电话: {phone}")
        
        create_phone_result = await client.contact_information.create_phone(
            vault_id=vault_id,
            contact_id=contact_id,
            phone=phone
        )
        
        if create_phone_result:
            print("\n创建电话成功:")
            print(json.dumps(create_phone_result, indent=2, ensure_ascii=False))
            
            # 从响应中提取 contact_information_id
            phone_info_id = None
            if 'data' in create_phone_result:
                data = create_phone_result['data']
                if isinstance(data, dict):
                    phone_info_id = str(data.get('id', ''))
                    print(f"\n创建的联系人信息 ID: {phone_info_id}")
            
            # 测试 3: 更新电话（如果创建成功）
            if phone_info_id:
                print("\n" + "=" * 50)
                print("测试 3: 更新电话")
                print("=" * 50)
                
                new_phone = "13800138000"
                print(f"新电话: {new_phone}")
                
                # 使用便捷方法更新电话
                update_result = await client.contact_information.update_phone(
                    vault_id=vault_id,
                    contact_id=contact_id,
                    contact_information_id=phone_info_id,
                    phone=new_phone
                )
                
                if update_result:
                    print("\n更新成功:")
                    print(json.dumps(update_result, indent=2, ensure_ascii=False))
                else:
                    print("更新失败")
                
                # 测试 4: 删除电话（如果更新成功）
                print("\n" + "=" * 50)
                print("测试 4: 删除电话")
                print("=" * 50)
                
                delete_result = await client.contact_information.delete(
                    vault_id=vault_id,
                    contact_id=contact_id,
                    contact_information_id=phone_info_id
                )
                
                if delete_result:
                    print("\n删除成功:")
                    print(json.dumps(delete_result, indent=2, ensure_ascii=False))
                else:
                    print("删除失败或已删除")
        else:
            print("创建电话失败")
        
        # 测试 5: 使用通用方法创建邮箱
        print("\n" + "=" * 50)
        print("测试 5: 使用通用方法创建邮箱")
        print("=" * 50)
        
        email2 = "test@example.com"
        print(f"邮箱: {email2}")
        
        create_result = await client.contact_information.create(
            vault_id=vault_id,
            contact_id=contact_id,
            data_value=email2,
            contact_information_type_id=1  # 1 = 邮箱
        )
        
        if create_result:
            print("\n创建成功:")
            print(json.dumps(create_result, indent=2, ensure_ascii=False))
        else:
            print("创建失败")
        
        print("\n" + "=" * 50)
        print("所有测试完成！")
        print("=" * 50)


if __name__ == "__main__":
    asyncio.run(main())

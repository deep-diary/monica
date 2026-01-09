"""
测试地址（Addresses）功能
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
        # 测试 1: 创建第二居所地址
        print("=" * 50)
        print("测试 1: 创建第二居所地址")
        print("=" * 50)
        
        address_data = {
            "line_1": "周巷镇开发路 68 号绿城惠园 33 栋 303 室",
            "line_2": "",
            "city": "宁波市",
            "province": "浙江省",
            "postal_code": "315324",
            "country": "中国",
            "address_type_id": client.addresses.ADDRESS_TYPE_SECONDARY  # 2 = 第二居所
        }
        
        print(f"地址类型: 第二居所 (ID: {address_data['address_type_id']})")
        print(f"地址: {address_data['line_1']}")
        print(f"城市: {address_data['city']}")
        print(f"省份: {address_data['province']}")
        print(f"邮编: {address_data['postal_code']}")
        print(f"国家: {address_data['country']}")
        
        create_result = await client.addresses.create(
            vault_id=vault_id,
            contact_id=contact_id,
            **address_data
        )
        
        if create_result:
            print("\n创建地址成功:")
            print(json.dumps(create_result, indent=2, ensure_ascii=False))
            
            # 从响应中提取 address_id
            address_id = None
            if 'data' in create_result:
                data = create_result['data']
                if isinstance(data, dict):
                    address_id = str(data.get('id', ''))
                    print(f"\n创建的地址 ID: {address_id}")
            
            # 测试 2: 更新地址（如果创建成功）
            if address_id:
                print("\n" + "=" * 50)
                print("测试 2: 更新地址")
                print("=" * 50)
                
                new_line_1 = "周巷镇开发路 68 号绿城惠园 33 栋 304 室"
                print(f"新地址: {new_line_1}")
                
                update_result = await client.addresses.update(
                    vault_id=vault_id,
                    contact_id=contact_id,
                    address_id=address_id,
                    line_1=new_line_1,
                    city=address_data["city"],
                    province=address_data["province"],
                    country=address_data["country"],
                    address_type_id=address_data["address_type_id"],
                    line_2=address_data["line_2"],
                    postal_code=address_data["postal_code"]
                )
                
                if update_result:
                    print("\n更新成功:")
                    print(json.dumps(update_result, indent=2, ensure_ascii=False))
                else:
                    print("更新失败")
                
                # 测试 3: 删除地址（如果更新成功）
                print("\n" + "=" * 50)
                print("测试 3: 删除地址")
                print("=" * 50)
                
                delete_result = await client.addresses.delete(
                    vault_id=vault_id,
                    contact_id=contact_id,
                    address_id=address_id
                )
                
                if delete_result:
                    print("\n删除成功:")
                    print(json.dumps(delete_result, indent=2, ensure_ascii=False))
                else:
                    print("删除失败或已删除")
        else:
            print("创建地址失败")
        
        # 测试 4: 创建不同类型的地址
        print("\n" + "=" * 50)
        print("测试 4: 创建不同类型的地址")
        print("=" * 50)
        
        address_types = {
            client.addresses.ADDRESS_TYPE_HOME: "主页",
            client.addresses.ADDRESS_TYPE_WORK: "工作",
            client.addresses.ADDRESS_TYPE_CABIN: "小木屋",
            client.addresses.ADDRESS_TYPE_OTHER: "其他"
        }
        
        for addr_type_id, addr_type_name in address_types.items():
            print(f"\n地址类型: {addr_type_name} (ID: {addr_type_id})")
            
            test_address = {
                "line_1": f"测试地址 {addr_type_name}",
                "city": "测试城市",
                "province": "测试省份",
                "country": "中国",
                "address_type_id": addr_type_id
            }
            
            result = await client.addresses.create(
                vault_id=vault_id,
                contact_id=contact_id,
                **test_address
            )
            
            if result:
                print(f"  ✓ 创建成功")
                if 'data' in result and isinstance(result['data'], dict):
                    addr_id = str(result['data'].get('id', ''))
                    # 可选：立即删除测试数据
                    # if addr_id:
                    #     await client.addresses.delete(
                    #         vault_id=vault_id,
                    #         contact_id=contact_id,
                    #         address_id=addr_id
                    #     )
                    #     print(f"  ✓ 已清理测试数据")
            else:
                print(f"  ✗ 创建失败")
        
        print("\n" + "=" * 50)
        print("所有测试完成！")
        print("=" * 50)


if __name__ == "__main__":
    asyncio.run(main())

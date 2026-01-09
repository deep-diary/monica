"""
测试 QuickFacts 功能
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
    vault_id = "019b83ae-f4bc-7360-bab1-84e226a00e43"  # friends vault
    
    # 创建客户端实例
    async with MonicaClient(monica_token, monica_base_url) as client:
        # 先获取一个联系人用于测试
        print("=" * 50)
        print("步骤 1: 获取联系人列表")
        print("=" * 50)
        
        contacts_data = await client.contacts.list(vault_id=vault_id, limit=5, page=1)
        contacts = client.contacts.extract_contacts_from_response(contacts_data) if contacts_data else []
        
        if not contacts:
            print("未找到联系人，无法进行测试")
            return
        
        contact = contacts[0]
        contact_id = contact.get('id')
        contact_name = contact.get('name', 'N/A')
        
        print(f"\n选择联系人: {contact_name} (ID: {contact_id})")
        
        # 测试模板 ID（根据文档，3 是"资源"类别）
        template_id = "3"  # 资源
        
        # 测试 1: 创建 QuickFact
        print("\n" + "=" * 50)
        print("测试 1: 创建 QuickFact")
        print("=" * 50)
        
        content = "擅长使用python 帮别人开发一些高效工具"
        print(f"模板 ID: {template_id} (资源)")
        print(f"内容: {content}")
        
        create_result = await client.quick_facts.create(
            vault_id=vault_id,
            contact_id=contact_id,
            template_id=template_id,
            content=content
        )
        
        if create_result:
            print("\n创建成功:")
            print(json.dumps(create_result, indent=2, ensure_ascii=False))
            
            # 从响应中提取 quick_fact_id
            quick_fact_id = None
            if 'data' in create_result:
                data = create_result['data']
                if isinstance(data, dict):
                    quick_fact_id = str(data.get('id', ''))
                    print(f"\n创建的 QuickFact ID: {quick_fact_id}")
                elif isinstance(data, str):
                    # 如果返回的是 URL，尝试从 URL 中提取 ID
                    if '/quickFacts/' in data:
                        parts = data.split('/quickFacts/')
                        if len(parts) > 1:
                            quick_fact_id = parts[1].split('/')[-1]
                            print(f"\n从 URL 提取的 QuickFact ID: {quick_fact_id}")
            
            if quick_fact_id:
                # 测试 2: 获取 QuickFact
                print("\n" + "=" * 50)
                print("测试 2: 获取 QuickFact")
                print("=" * 50)
                
                get_result = await client.quick_facts.get(
                    vault_id=vault_id,
                    contact_id=contact_id,
                    template_id=template_id
                )
                
                if get_result:
                    print("\n获取成功:")
                    print(json.dumps(get_result, indent=2, ensure_ascii=False)[:500] + "...")
                
                # 测试 3: 更新 QuickFact
                print("\n" + "=" * 50)
                print("测试 3: 更新 QuickFact")
                print("=" * 50)
                
                new_content = "擅长使用 Python 和 AI 技术帮别人开发高效工具和自动化解决方案"
                print(f"新内容: {new_content}")
                
                update_result = await client.quick_facts.update(
                    vault_id=vault_id,
                    contact_id=contact_id,
                    template_id=template_id,
                    quick_fact_id=quick_fact_id,
                    content=new_content
                )
                
                if update_result:
                    print("\n更新成功:")
                    print(json.dumps(update_result, indent=2, ensure_ascii=False))
                else:
                    print("更新失败")
                
                # 测试 4: 删除 QuickFact
                print("\n" + "=" * 50)
                print("测试 4: 删除 QuickFact")
                print("=" * 50)
                
                delete_result = await client.quick_facts.delete(
                    vault_id=vault_id,
                    contact_id=contact_id,
                    template_id=template_id,
                    quick_fact_id=quick_fact_id
                )
                
                if delete_result:
                    print("\n删除成功:")
                    print(json.dumps(delete_result, indent=2, ensure_ascii=False))
                else:
                    print("删除失败或已删除")
            else:
                print("\n警告: 无法从创建响应中提取 QuickFact ID，跳过后续测试")
        else:
            print("创建失败")
        
        # 测试 5: 测试其他模板
        print("\n" + "=" * 50)
        print("测试 5: 创建不同类型的 QuickFact")
        print("=" * 50)
        
        templates = {
            "3": "兴趣爱好",
            "4": "食物偏好",
            "11": "资源",
            "12": "需求"
        }
        
        for template_id, template_name in templates.items():
            print(f"\n模板: {template_name} (ID: {template_id})")
            test_content = f"这是一个测试的{template_name}内容"
            
            result = await client.quick_facts.create(
                vault_id=vault_id,
                contact_id=contact_id,
                template_id=template_id,
                content=test_content
            )
            
            if result:
                print(f"  ✓ 创建成功")
                if 'data' in result and isinstance(result['data'], dict):
                    qf_id = str(result['data'].get('id', ''))
                    # if qf_id:
                    #     # 立即删除测试数据
                    #     await client.quick_facts.delete(
                    #         vault_id=vault_id,
                    #         contact_id=contact_id,
                    #         template_id=template_id,
                    #         quick_fact_id=qf_id
                    #     )
                    #     print(f"  ✓ 已清理测试数据")
            else:
                print(f"  ✗ 创建失败")
        
        print("\n" + "=" * 50)
        print("所有测试完成！")
        print("=" * 50)


if __name__ == "__main__":
    asyncio.run(main())

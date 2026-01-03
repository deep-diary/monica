"""
测试 PyMonica 包的功能
"""

import json
import sys
import os

# 添加父目录到路径，以便导入 pymonica 包
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pymonica import MonicaClient


def main():
    # 配置信息
    # monica_token = "DcmeEW7FLD4ly8EkhOI9ZBjfKXxre3eTq5m6hTJq1ef2f025"  # mac
    monica_token = "8m3ihVnLHt8B7QeuWn7GJdDCKEqwNoe7hVKtSugZ576f1c46"  # win
    monica_base_url = "http://192.168.31.25:8080"
    vault_id = "019b6548-e77c-73ad-8431-846334b79395"  # DeepDiary vault
    
    # 创建客户端实例
    client = MonicaClient(monica_token, monica_base_url)
    
    # 测试 1: 获取当前用户信息
    print("=" * 50)
    print("测试 1: 获取当前用户信息")
    print("=" * 50)
    user_data = client.get_current_user()
    
    if user_data:
        print("\n用户信息:")
        print(json.dumps(user_data, indent=2, ensure_ascii=False))
        
        # 提取并显示关键信息
        if 'data' in user_data:
            user = user_data['data']
            print(f"\n用户 ID: {user.get('id')}")
            print(f"姓名: {user.get('name')}")
            print(f"邮箱: {user.get('email')}")
            print(f"创建时间: {user.get('created_at')}")
    else:
        print("获取用户信息失败")
        return
    
    # 测试 2: 获取 Vault 列表
    print("\n" + "=" * 50)
    print("测试 2: 获取 Vault 列表")
    print("=" * 50)
    vaults_data = client.get_vaults()
    
    if vaults_data:
        print("\nVault 列表:")
        if 'data' in vaults_data and isinstance(vaults_data['data'], list):
            vaults = vaults_data['data']
            print(f"共找到 {len(vaults)} 个 Vault:")
            for vault in vaults:
                print(f"  - {vault.get('name')} (ID: {vault.get('id')})")
    
    # 测试 3: 获取联系人列表
    print("\n" + "=" * 50)
    print("测试 3: 获取联系人列表")
    print("=" * 50)
    print(f"Vault ID: {vault_id}")
    print()
    
    contacts_data = client.contacts.list(vault_id=vault_id, limit=25, page=1)
    
    if contacts_data:
        # 使用辅助方法提取联系人
        contacts = client.contacts.extract_contacts_from_response(contacts_data)
        
        # 提取分页信息
        paginator = None
        if 'props' in contacts_data and 'data' in contacts_data['props']:
            paginator = contacts_data['props']['data'].get('paginator', {})
        elif 'data' in contacts_data:
            if isinstance(contacts_data['data'], dict):
                paginator = contacts_data['data'].get('paginator', {})
        
        if contacts:
            total = paginator.get('total', len(contacts)) if paginator else len(contacts)
            print(f"\n共找到 {total} 个联系人 (当前页显示 {len(contacts)} 个):")
            print()
            for i, contact in enumerate(contacts, 1):
                print(f"联系人 {i}:")
                print(f"  ID: {contact.get('id')}")
                print(f"  姓名: {contact.get('name', 'N/A')}")
                if 'url' in contact and 'show' in contact['url']:
                    print(f"  详情链接: {contact['url']['show']}")
                print()
        else:
            print("\n未找到联系人数据，完整响应:")
            print(json.dumps(contacts_data, indent=2, ensure_ascii=False)[:1000] + "...")
    else:
        print("获取联系人列表失败")
        return
    
    # 测试 4: 创建联系人
    print("\n" + "=" * 50)
    print("测试 4: 创建联系人")
    print("=" * 50)
    
    new_contact = client.contacts.create(
        vault_id=vault_id,
        first_name="test",
        last_name="ge",
        nickname="测试昵称",
        gender_id="1"
    )
    
    if new_contact:
        print("\n创建联系人成功:")
        print(json.dumps(new_contact, indent=2, ensure_ascii=False))
        
        # 从响应中提取联系人 ID
        contact_url = new_contact.get('data', '')
        if contact_url:
            # 从 URL 中提取 ID: http://.../contacts/{id}
            contact_id = contact_url.split('/contacts/')[-1] if '/contacts/' in contact_url else None
            
            if contact_id:
                print(f"\n新创建的联系人 ID: {contact_id}")
                
                # 测试 5: 获取单个联系人详情
                print("\n" + "=" * 50)
                print("测试 5: 获取单个联系人详情")
                print("=" * 50)
                
                contact_detail = client.contacts.get(vault_id, contact_id)
                if contact_detail:
                    print("\n联系人详情:")
                    print(json.dumps(contact_detail, indent=2, ensure_ascii=False)[:500] + "...")
                
                # 测试 6: 更新联系人
                print("\n" + "=" * 50)
                print("测试 6: 更新联系人")
                print("=" * 50)
                
                updated_contact = client.contacts.update(
                    vault_id=vault_id,
                    contact_id=contact_id,
                    first_name="test_updated",
                    last_name="ge",
                    nickname="新昵称"
                )
                
                if updated_contact:
                    print("\n更新联系人成功")
                    print(json.dumps(updated_contact, indent=2, ensure_ascii=False)[:500] + "...")
                else:
                    print("更新联系人失败")
                
                # 测试 7: 删除联系人
                print("\n" + "=" * 50)
                print("测试 7: 删除联系人")
                print("=" * 50)
                
                delete_result = client.contacts.delete(vault_id, contact_id)
                if delete_result:
                    print("\n删除联系人成功:")
                    print(json.dumps(delete_result, indent=2, ensure_ascii=False))
                else:
                    print("删除联系人失败（可能已删除或不存在）")
            else:
                print("无法从响应中提取联系人 ID")
        else:
            print("创建响应中没有找到联系人 URL")
    else:
        print("创建联系人失败")
    
    # 测试 8: 搜索联系人
    print("\n" + "=" * 50)
    print("测试 8: 搜索联系人")
    print("=" * 50)
    
    # 先获取一个联系人用于搜索测试
    if contacts_data:
        contacts = client.contacts.extract_contacts_from_response(contacts_data)
        if contacts:
            search_name = contacts[0].get('name', '').split()[0] if contacts[0].get('name') else "葛"
            print(f"搜索关键词: {search_name}")
            
            search_results = client.contacts.search(vault_id, search_name)
            if search_results:
                print("\n搜索结果:")
                print(json.dumps(search_results, indent=2, ensure_ascii=False)[:500] + "...")
            else:
                print("搜索失败")
    
    print("\n" + "=" * 50)
    print("所有测试完成！")
    print("=" * 50)


if __name__ == "__main__":
    main()

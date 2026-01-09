"""
测试联系人信息提取器（ContactInformationExtractor）功能
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
        # 测试 1: 获取完整的联系人信息
        print("=" * 50)
        print("测试 1: 获取完整的联系人信息")
        print("=" * 50)
        
        full_info = await client.contact_info.get_full_information(vault_id, contact_id)
        if full_info:
            print("✓ 成功获取完整联系人信息")
            # 打印基本信息结构
            if 'props' in full_info and 'data' in full_info['props']:
                data = full_info['props']['data']
                # 使用提取器的方法获取ID和名称
                contact_id_extracted = client.contact_info.get_contact_id(full_info)
                contact_name_extracted = client.contact_info.get_contact_name(full_info)
                print(f"  联系人 ID: {contact_id_extracted or 'N/A'}")
                print(f"  联系人名称: {contact_name_extracted or 'N/A'}")
                if 'modules' in data:
                    print(f"  模块数量: {len(data['modules'])}")
                    module_types = [m.get('type', 'unknown') for m in data['modules'] if isinstance(m, dict)]
                    print(f"  模块类型: {', '.join(module_types)}")
        else:
            print("✗ 获取失败")
        
        # 测试 2: 获取所有模块的数据
        print("\n" + "=" * 50)
        print("测试 2: 获取所有模块的数据")
        print("=" * 50)
        
        all_modules = await client.contact_info.get_all_modules(vault_id, contact_id)
        if all_modules:
            print(f"✓ 成功获取 {len(all_modules)} 个模块的数据:")
            for module_type, module_data in all_modules.items():
                if isinstance(module_data, list):
                    print(f"  - {module_type}: {len(module_data)} 条记录")
                    # 如果是地址或联系信息，显示前几条的详细信息
                    if module_type in ['addresses', 'address', 'contactInformation', 'contact_information'] and len(module_data) > 0:
                        print(f"    示例: {json.dumps(module_data[0], indent=6, ensure_ascii=False)[:200]}...")
                elif isinstance(module_data, dict):
                    print(f"  - {module_type}: 字典数据")
                    # 打印字典的键
                    if module_data:
                        print(f"    键: {', '.join(list(module_data.keys())[:10])}")
                else:
                    print(f"  - {module_type}: {type(module_data).__name__}")
        else:
            print("✗ 获取失败")
        
        # 调试：打印所有模块类型
        print("\n调试信息：所有模块类型")
        full_info = await client.contact_info.get_full_information(vault_id, contact_id, use_cache=False)
        if full_info and 'props' in full_info and 'data' in full_info['props']:
            data = full_info['props']['data']
            if 'modules' in data:
                print(f"  模块列表:")
                for idx, module in enumerate(data['modules']):
                    if isinstance(module, dict):
                        module_type = module.get('type', 'unknown')
                        module_data = module.get('data', {})
                        print(f"    {idx+1}. type: {module_type}")
                        if isinstance(module_data, dict):
                            print(f"       data 键: {', '.join(list(module_data.keys())[:10])}")
                        elif isinstance(module_data, list):
                            print(f"       data 类型: list (长度: {len(module_data)})")
            # 也检查 data 的直接键
            print(f"  data 直接键: {', '.join([k for k in data.keys() if k != 'modules'][:20])}")
        
        # 测试 3: 获取通话记录
        print("\n" + "=" * 50)
        print("测试 3: 获取通话记录")
        print("=" * 50)
        
        calls = await client.contact_info.get_calls(vault_id, contact_id)
        if calls:
            print(f"✓ 成功获取 {len(calls)} 条通话记录")
            for idx, call in enumerate(calls[:3], 1):  # 只显示前3条
                print(f"  {idx}. ID: {call.get('id')}, 日期: {call.get('called_at')}, 类型: {call.get('type')}")
        else:
            print("  未找到通话记录")
        
        # 测试 4: 获取提醒事项
        print("\n" + "=" * 50)
        print("测试 4: 获取提醒事项")
        print("=" * 50)
        
        reminders = await client.contact_info.get_reminders(vault_id, contact_id)
        if reminders:
            print(f"✓ 成功获取 {len(reminders)} 条提醒事项")
            for idx, reminder in enumerate(reminders[:3], 1):  # 只显示前3条
                print(f"  {idx}. ID: {reminder.get('id')}, 标签: {reminder.get('label')}, 日期: {reminder.get('date')}")
        else:
            print("  未找到提醒事项")
        
        # 测试 5: 获取笔记
        print("\n" + "=" * 50)
        print("测试 5: 获取笔记")
        print("=" * 50)
        
        notes = await client.contact_info.get_notes(vault_id, contact_id)
        if notes:
            print(f"✓ 成功获取 {len(notes)} 条笔记")
            for idx, note in enumerate(notes[:3], 1):  # 只显示前3条
                print(f"  {idx}. ID: {note.get('id')}, 标题: {note.get('title', 'N/A')}")
        else:
            print("  未找到笔记")
        
        # 测试 6: 获取地址
        print("\n" + "=" * 50)
        print("测试 6: 获取地址")
        print("=" * 50)
        
        addresses = await client.contact_info.get_addresses(vault_id, contact_id)
        if addresses:
            print(f"✓ 成功获取 {len(addresses)} 个地址")
            for idx, address in enumerate(addresses[:3], 1):  # 只显示前3个
                line_1 = address.get('line_1', '')
                city = address.get('city', '')
                province = address.get('province', '')
                country = address.get('country', '')
                address_type = address.get('type', {})
                type_name = address_type.get('name', 'N/A') if isinstance(address_type, dict) else 'N/A'
                print(f"  {idx}. ID: {address.get('id')}, 类型: {type_name}")
                print(f"     地址: {line_1}, {city}, {province}, {country}")
        else:
            print("  未找到地址")
        
        # 测试 6.1: 获取地址（包含非活动地址）
        print("\n" + "=" * 50)
        print("测试 6.1: 获取地址（包含非活动地址）")
        print("=" * 50)
        
        all_addresses = await client.contact_info.get_addresses(vault_id, contact_id, include_inactive=True)
        if all_addresses:
            print(f"✓ 成功获取 {len(all_addresses)} 个地址（包含非活动地址）")
        else:
            print("  未找到地址")
        
        # 测试 7: 获取联系信息（邮箱、电话等）
        print("\n" + "=" * 50)
        print("测试 7: 获取联系信息")
        print("=" * 50)
        
        contact_info_list = await client.contact_info.get_contact_information(vault_id, contact_id)
        if contact_info_list:
            print(f"✓ 成功获取 {len(contact_info_list)} 条联系信息")
            for idx, info in enumerate(contact_info_list[:5], 1):  # 只显示前5条
                info_type = info.get('contact_information_type', {})
                info_type_name = info_type.get('name', '未知') if isinstance(info_type, dict) else '未知'
                data_value = info.get('data', 'N/A')
                label = info.get('label', data_value)
                print(f"  {idx}. ID: {info.get('id')}, 类型: {info_type_name}, 数据: {data_value}, 标签: {label}")
        else:
            print("  未找到联系信息")
        
        # 测试 8: 获取日期（生日、纪念日等）
        print("\n" + "=" * 50)
        print("测试 8: 获取日期（重要的日子）")
        print("=" * 50)
        
        dates = await client.contact_info.get_dates(vault_id, contact_id)
        if dates:
            print(f"✓ 成功获取 {len(dates)} 个日期")
            for idx, date_item in enumerate(dates[:5], 1):  # 只显示前5个
                date_id = date_item.get('id')
                label = date_item.get('label', 'N/A')
                date_str = date_item.get('date', 'N/A')
                date_type = date_item.get('type', 'N/A')
                age = date_item.get('age', 'N/A')
                print(f"  {idx}. ID: {date_id}, 标签: {label}, 日期: {date_str}, 类型: {date_type}, 年龄: {age}")
        else:
            print("  未找到日期")
        
        # 测试 12: 获取快速事实（Quick Facts）
        print("\n" + "=" * 50)
        print("测试 12: 获取快速事实（Quick Facts）")
        print("=" * 50)
        
        quick_facts_data = await client.contact_info.get_quick_facts(vault_id, contact_id)
        if quick_facts_data:
            print("✓ 成功获取快速事实数据")
            print(f"  显示快速事实: {quick_facts_data.get('show_quick_facts', 'N/A')}")
            
            templates = quick_facts_data.get('templates', [])
            if templates:
                print(f"  模板数量: {len(templates)}")
                for idx, template in enumerate(templates[:4], 1):
                    template_id = template.get('id', 'N/A')
                    template_label = template.get('label', 'N/A')
                    print(f"    {idx}. ID: {template_id}, 标签: {template_label}")
            
            quick_facts_obj = quick_facts_data.get('quick_facts', {})
            # quick_facts 是一个字典，包含 template 和 quick_facts 键
            if isinstance(quick_facts_obj, dict):
                template = quick_facts_obj.get('template', {})
                if template:
                    template_id = template.get('id', 'N/A')
                    template_label = template.get('label', 'N/A')
                    print(f"  当前模板: ID {template_id}, 标签: {template_label}")
                
                quick_facts_list = quick_facts_obj.get('quick_facts', [])
                if isinstance(quick_facts_list, list) and quick_facts_list:
                    print(f"  快速事实数量: {len(quick_facts_list)}")
                    for idx, fact in enumerate(quick_facts_list[:5], 1):
                        fact_id = fact.get('id', 'N/A')
                        fact_content = fact.get('content', fact.get('data', 'N/A'))
                        print(f"    {idx}. ID: {fact_id}, 内容: {fact_content}")
                else:
                    print("  未找到快速事实列表")
            elif isinstance(quick_facts_obj, list):
                print(f"  快速事实数量: {len(quick_facts_obj)}")
                for idx, fact in enumerate(quick_facts_obj[:5], 1):
                    fact_id = fact.get('id', 'N/A')
                    fact_content = fact.get('content', fact.get('data', 'N/A'))
                    print(f"    {idx}. ID: {fact_id}, 内容: {fact_content}")
            else:
                print("  未找到快速事实列表")
        else:
            print("  未找到快速事实数据")
        
        # 测试 12.1: 获取快速事实列表（便捷方法）
        print("\n" + "=" * 50)
        print("测试 12.1: 获取快速事实列表（便捷方法）")
        print("=" * 50)
        
        quick_facts_list = await client.contact_info.get_quick_facts_list(vault_id, contact_id)
        if quick_facts_list:
            print(f"✓ 成功获取 {len(quick_facts_list)} 条快速事实")
            for idx, fact in enumerate(quick_facts_list[:5], 1):
                fact_id = fact.get('id', 'N/A')
                fact_content = fact.get('content', fact.get('data', fact.get('value', 'N/A')))
                print(f"  {idx}. ID: {fact_id}, 内容: {fact_content}")
        else:
            print("  未找到快速事实")
        
        # 测试 9: 测试缓存功能
        print("\n" + "=" * 50)
        print("测试 9: 测试缓存功能")
        print("=" * 50)
        
        import time
        start_time = time.time()
        calls1 = await client.contact_info.get_calls(vault_id, contact_id, use_cache=True)
        time1 = time.time() - start_time
        
        start_time = time.time()
        calls2 = await client.contact_info.get_calls(vault_id, contact_id, use_cache=True)
        time2 = time.time() - start_time
        
        print(f"第一次获取（无缓存）: {time1:.3f} 秒")
        print(f"第二次获取（使用缓存）: {time2:.3f} 秒")
        if time2 < time1:
            print("✓ 缓存功能正常工作")
        else:
            print("  缓存可能未生效")
        
        # 测试 10: 清除缓存
        print("\n" + "=" * 50)
        print("测试 10: 清除缓存")
        print("=" * 50)
        
        client.contact_info.clear_cache()
        print("✓ 缓存已清除")
        
        # 测试 11: 使用通用方法获取模块数据
        print("\n" + "=" * 50)
        print("测试 11: 使用通用方法获取模块数据")
        print("=" * 50)
        
        custom_module = await client.contact_info.get_module_by_type(vault_id, contact_id, 'calls')
        if custom_module:
            print(f"✓ 成功使用通用方法获取 calls 模块: {len(custom_module) if isinstance(custom_module, list) else 'N/A'} 条记录")
        else:
            print("  未找到模块数据")
        
        # 测试 13: 获取所有信息并以JSON格式输出
        print("\n" + "=" * 50)
        print("测试 13: 获取所有信息并以JSON格式输出")
        print("=" * 50)
        
        all_info_json = await client.contact_info.get_all_information_as_json(vault_id, contact_id)
        if all_info_json:
            print("✓ 成功获取所有信息（JSON格式）:")
            print(all_info_json)
        else:
            print("✗ 获取失败")
        
        print("\n" + "=" * 50)
        print("所有测试完成！")
        print("=" * 50)


if __name__ == "__main__":
    asyncio.run(main())

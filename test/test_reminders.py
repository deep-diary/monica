"""
测试提醒事项（Reminders）功能
"""

import json
import sys
import os
import asyncio
from datetime import datetime

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
        # 测试 1: 创建提醒事项
        print("=" * 50)
        print("测试 1: 创建提醒事项")
        print("=" * 50)
        
        # 使用未来日期作为提醒日期
        future_date = "2026-01-09"
        
        reminder_data = {
            "label": "test remender",
            "reminder_choice": client.reminders.REMINDER_CHOICE_ONE_TIME,
            "day": "",
            "month": "",
            "choice": client.reminders.CHOICE_FULL_DATE,
            "date": future_date,
            "frequency_type": client.reminders.FREQUENCY_TYPE_RECURRING_YEAR,
            "frequency_number": 1
        }
        
        print(f"标签: {reminder_data['label']}")
        print(f"提醒类型: {reminder_data['reminder_choice']}")
        print(f"日期选择类型: {reminder_data['choice']}")
        print(f"日期: {reminder_data['date']}")
        print(f"频率类型: {reminder_data['frequency_type']}")
        print(f"频率数字: {reminder_data['frequency_number']}")
        
        create_result = await client.reminders.create(
            vault_id=vault_id,
            contact_id=contact_id,
            **reminder_data
        )
        
        if create_result:
            print("\n创建提醒事项成功:")
            print(json.dumps(create_result, indent=2, ensure_ascii=False))
            
            # 从响应中提取 reminder_id
            reminder_id = None
            if isinstance(create_result, dict):
                # 检查响应格式，可能直接是字典或包含 data 字段
                if 'id' in create_result:
                    reminder_id = str(create_result.get('id', ''))
                elif 'data' in create_result:
                    data = create_result['data']
                    if isinstance(data, dict) and 'id' in data:
                        reminder_id = str(data.get('id', ''))
            
            if reminder_id:
                print(f"\n创建的提醒事项 ID: {reminder_id}")
                
                # 测试 2: 获取提醒事项列表（通过联系人详情页面）
                print("\n" + "=" * 50)
                print("测试 2: 获取提醒事项列表")
                print("=" * 50)
                
                reminders_list = await client.reminders.list(
                    vault_id=vault_id,
                    contact_id=contact_id
                )
                
                if reminders_list:
                    print(f"\n获取到 {len(reminders_list)} 条提醒事项:")
                    for idx, reminder in enumerate(reminders_list[:5], 1):  # 只显示前5条
                        print(f"  {idx}. ID: {reminder.get('id')}, 标签: {reminder.get('label')}, 日期: {reminder.get('date')}")
                else:
                    print("未获取到提醒事项（可能联系人详情页面中不包含 reminders 字段）")
                
                # 测试 3: 获取单个提醒事项（如果列表获取成功）
                if reminders_list and len(reminders_list) > 0:
                    print("\n" + "=" * 50)
                    print("测试 3: 获取单个提醒事项")
                    print("=" * 50)
                    
                    first_reminder_id = reminders_list[0].get('id')
                    if first_reminder_id:
                        get_result = await client.reminders.get(
                            vault_id=vault_id,
                            contact_id=contact_id,
                            reminder_id=str(first_reminder_id)
                        )
                        
                        if get_result:
                            print("\n获取提醒事项成功:")
                            print(json.dumps(get_result, indent=2, ensure_ascii=False))
                        else:
                            print("获取提醒事项失败")
                
                # 测试 4: 更新提醒事项（如果创建成功）
                print("\n" + "=" * 50)
                print("测试 4: 更新提醒事项")
                print("=" * 50)
                
                new_label = "test remender update"
                new_date = "2026-01-10"
                print(f"新标签: {new_label}")
                print(f"新日期: {new_date}")
                
                update_result = await client.reminders.update(
                    vault_id=vault_id,
                    contact_id=contact_id,
                    reminder_id=reminder_id,
                    label=new_label,
                    reminder_choice=client.reminders.REMINDER_CHOICE_RECURRING,
                    day=10,
                    month=1,
                    choice=client.reminders.CHOICE_FULL_DATE,
                    date=new_date,
                    frequency_type=client.reminders.FREQUENCY_TYPE_RECURRING_YEAR,
                    frequency_number=1
                )
                
                if update_result:
                    print("\n更新成功:")
                    print(json.dumps(update_result, indent=2, ensure_ascii=False))
                else:
                    print("更新失败")
                
                # 测试 5: 删除提醒事项（如果更新成功）
                print("\n" + "=" * 50)
                print("测试 5: 删除提醒事项")
                print("=" * 50)
                
                delete_result = await client.reminders.delete(
                    vault_id=vault_id,
                    contact_id=contact_id,
                    reminder_id=reminder_id
                )
                
                if delete_result:
                    print("\n删除成功:")
                    print(json.dumps(delete_result, indent=2, ensure_ascii=False))
                else:
                    print("删除失败或已删除")
            else:
                print("\n警告: 无法从响应中提取提醒事项 ID")
        else:
            print("创建提醒事项失败")
        
        # 测试 6: 创建不同类型的提醒事项
        print("\n" + "=" * 50)
        print("测试 6: 创建不同类型的提醒事项")
        print("=" * 50)
        
        reminder_types = {
            client.reminders.REMINDER_CHOICE_ONE_TIME: "一次性提醒",
            client.reminders.REMINDER_CHOICE_RECURRING: "重复提醒"
        }
        
        created_reminder_ids = []
        
        for reminder_type, reminder_type_name in reminder_types.items():
            print(f"\n提醒类型: {reminder_type_name} ({reminder_type})")
            
            test_reminder = {
                "label": f"测试 {reminder_type_name}",
                "reminder_choice": reminder_type,
                "day": "",
                "month": "",
                "choice": client.reminders.CHOICE_FULL_DATE,
                "date": future_date,
                "frequency_type": client.reminders.FREQUENCY_TYPE_RECURRING_YEAR,
                "frequency_number": 1
            }
            
            result = await client.reminders.create(
                vault_id=vault_id,
                contact_id=contact_id,
                **test_reminder
            )
            
            if result:
                print(f"  ✓ 创建成功")
                # 提取 ID 用于后续清理
                reminder_id_to_clean = None
                if isinstance(result, dict) and 'id' in result:
                    reminder_id_to_clean = str(result.get('id', ''))
                elif isinstance(result, dict) and 'data' in result:
                    data = result['data']
                    if isinstance(data, dict) and 'id' in data:
                        reminder_id_to_clean = str(data.get('id', ''))
                if reminder_id_to_clean:
                    created_reminder_ids.append(reminder_id_to_clean)
            else:
                print(f"  ✗ 创建失败")
        
        # 清理测试数据
        if created_reminder_ids:
            print("\n清理测试数据...")
            for test_reminder_id in created_reminder_ids:
                await client.reminders.delete(
                    vault_id=vault_id,
                    contact_id=contact_id,
                    reminder_id=test_reminder_id
                )
            print(f"已清理 {len(created_reminder_ids)} 条测试数据")
        
        print("\n" + "=" * 50)
        print("所有测试完成！")
        print("=" * 50)


if __name__ == "__main__":
    asyncio.run(main())

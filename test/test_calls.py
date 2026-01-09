"""
测试通话记录（Calls）功能
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
        # 测试 1: 创建通话记录
        print("=" * 50)
        print("测试 1: 创建通话记录")
        print("=" * 50)
        
        # 使用当前日期作为通话日期
        today = datetime.now().strftime("%Y-%m-%d")
        
        call_data = {
            "who_initiated": client.calls.WHO_INITIATED_ME,
            "called_at": today,
            "call_reason_id": 5,
            "description": "这里是描述",
            "emotion_id": 3,
            "call_type": client.calls.CALL_TYPE_AUDIO
        }
        
        print(f"发起人: {call_data['who_initiated']}")
        print(f"通话日期: {call_data['called_at']}")
        print(f"通话原因 ID: {call_data['call_reason_id']}")
        print(f"描述: {call_data['description']}")
        print(f"情绪 ID: {call_data['emotion_id']}")
        print(f"通话类型: {call_data['call_type']}")
        
        create_result = await client.calls.create(
            vault_id=vault_id,
            contact_id=contact_id,
            **call_data
        )
        
        if create_result:
            print("\n创建通话记录成功:")
            print(json.dumps(create_result, indent=2, ensure_ascii=False))
            
            # 从响应中提取 call_id
            call_id = None
            if isinstance(create_result, dict):
                # 检查响应格式，可能直接是字典或包含 data 字段
                if 'id' in create_result:
                    call_id = str(create_result.get('id', ''))
                elif 'data' in create_result:
                    data = create_result['data']
                    if isinstance(data, dict) and 'id' in data:
                        call_id = str(data.get('id', ''))
            
            if call_id:
                print(f"\n创建的通话记录 ID: {call_id}")
                
                # 测试 2: 获取通话记录列表（通过联系人详情页面）
                print("\n" + "=" * 50)
                print("测试 2: 获取通话记录列表")
                print("=" * 50)
                
                calls_list = await client.calls.list(
                    vault_id=vault_id,
                    contact_id=contact_id
                )
                
                if calls_list:
                    print(f"\n获取到 {len(calls_list)} 条通话记录:")
                    for idx, call in enumerate(calls_list[:5], 1):  # 只显示前5条
                        print(f"  {idx}. ID: {call.get('id')}, 日期: {call.get('called_at')}, 类型: {call.get('type')}")
                else:
                    print("未获取到通话记录（可能联系人详情页面中不包含 calls 字段）")
                
                # 测试 3: 获取单个通话记录（如果列表获取成功）
                if calls_list and len(calls_list) > 0:
                    print("\n" + "=" * 50)
                    print("测试 3: 获取单个通话记录")
                    print("=" * 50)
                    
                    first_call_id = calls_list[0].get('id')
                    if first_call_id:
                        get_result = await client.calls.get(
                            vault_id=vault_id,
                            contact_id=contact_id,
                            call_id=str(first_call_id)
                        )
                        
                        if get_result:
                            print("\n获取通话记录成功:")
                            print(json.dumps(get_result, indent=2, ensure_ascii=False))
                        else:
                            print("获取通话记录失败")
                
                # 测试 4: 更新通话记录（如果创建成功）
                print("\n" + "=" * 50)
                print("测试 4: 更新通话记录")
                print("=" * 50)
                
                new_description = "更新后的描述"
                print(f"新描述: {new_description}")
                
                update_result = await client.calls.update(
                    vault_id=vault_id,
                    contact_id=contact_id,
                    call_id=call_id,
                    who_initiated=client.calls.WHO_INITIATED_CONTACT,
                    called_at=today,
                    call_reason_id=5,
                    description=new_description,
                    emotion_id=3,
                    call_type=client.calls.CALL_TYPE_VIDEO
                )
                
                if update_result:
                    print("\n更新成功:")
                    print(json.dumps(update_result, indent=2, ensure_ascii=False))
                else:
                    print("更新失败")
                
                # 测试 5: 删除通话记录（如果更新成功）
                print("\n" + "=" * 50)
                print("测试 5: 删除通话记录")
                print("=" * 50)
                
                delete_result = await client.calls.delete(
                    vault_id=vault_id,
                    contact_id=contact_id,
                    call_id=call_id
                )
                
                if delete_result:
                    print("\n删除成功:")
                    print(json.dumps(delete_result, indent=2, ensure_ascii=False))
                else:
                    print("删除失败或已删除")
            else:
                print("\n警告: 无法从响应中提取通话记录 ID")
        else:
            print("创建通话记录失败")
        
        # # 测试 6: 创建不同类型的通话记录
        # print("\n" + "=" * 50)
        # print("测试 6: 创建不同类型的通话记录")
        # print("=" * 50)
        
        # call_types = {
        #     client.calls.CALL_TYPE_AUDIO: "音频通话",
        #     client.calls.CALL_TYPE_VIDEO: "视频通话"
        # }
        
        # for call_type, call_type_name in call_types.items():
        #     print(f"\n通话类型: {call_type_name} ({call_type})")
            
        #     test_call = {
        #         "who_initiated": client.calls.WHO_INITIATED_ME,
        #         "called_at": today,
        #         "call_reason_id": 5,
        #         "description": f"测试 {call_type_name}",
        #         "emotion_id": 3,
        #         "call_type": call_type
        #     }
            
        #     result = await client.calls.create(
        #         vault_id=vault_id,
        #         contact_id=contact_id,
        #         **test_call
        #     )
            
        #     if result:
        #         print(f"  ✓ 创建成功")
        #         # 可选：提取 ID 并删除测试数据
        #         # call_id = None
        #         # if isinstance(result, dict) and 'id' in result:
        #         #     call_id = str(result.get('id', ''))
        #         # elif isinstance(result, dict) and 'data' in result:
        #         #     data = result['data']
        #         #     if isinstance(data, dict) and 'id' in data:
        #         #         call_id = str(data.get('id', ''))
        #         # if call_id:
        #         #     await client.calls.delete(
        #         #         vault_id=vault_id,
        #         #         contact_id=contact_id,
        #         #         call_id=call_id
        #         #     )
        #         #     print(f"  ✓ 已清理测试数据")
        #     else:
        #         print(f"  ✗ 创建失败")
        
        # 测试 7: 获取最后一次通话记录
        print("\n" + "=" * 50)
        print("测试 7: 获取最后一次通话记录")
        print("=" * 50)
        
        last_call = await client.calls.get_last_call(
            vault_id=vault_id,
            contact_id=contact_id
        )
        
        if last_call:
            print("\n最后一次通话记录:")
            print(json.dumps(last_call, indent=2, ensure_ascii=False))
        else:
            print("未找到通话记录")
        
        # 测试 8: 获取上次通话到现在的时间间隔
        print("\n" + "=" * 50)
        print("测试 8: 获取上次通话到现在的时间间隔")
        print("=" * 50)
        
        time_info = await client.calls.get_time_since_last_call(
            vault_id=vault_id,
            contact_id=contact_id
        )
        
        if time_info:
            print("\n时间间隔信息:")
            print(f"  距离今天: {time_info.get('formatted', 'N/A')}")
            print(f"  天数: {time_info.get('days_since', 'N/A')} 天")
            print(f"  周数: {time_info.get('weeks_since', 'N/A')} 周")
            print(f"  月数: {time_info.get('months_since', 'N/A')} 月")
            print(f"  年数: {time_info.get('years_since', 'N/A')} 年")
            print(f"\n最后一次通话详情:")
            last_call_detail = time_info.get('last_call', {})
            print(f"  ID: {last_call_detail.get('id', 'N/A')}")
            print(f"  日期: {last_call_detail.get('called_at', 'N/A')}")
            print(f"  类型: {last_call_detail.get('type', 'N/A')}")
            print(f"  发起人: {last_call_detail.get('who_initiated', 'N/A')}")
            print(f"  描述: {last_call_detail.get('description', 'N/A')}")
            print(f"  情绪: {last_call_detail.get('emotion', {}).get('name', 'N/A') if last_call_detail.get('emotion') else 'N/A'}")
            print(f"  原因: {last_call_detail.get('reason', {}).get('label', 'N/A') if last_call_detail.get('reason') else 'N/A'}")
        else:
            print("未找到通话记录或无法计算时间间隔")
        
        print("\n" + "=" * 50)
        print("所有测试完成！")
        print("=" * 50)


if __name__ == "__main__":
    asyncio.run(main())

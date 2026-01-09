"""
测试笔记（Notes）功能
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
        # 测试 1: 创建笔记
        print("=" * 50)
        print("测试 1: 创建笔记")
        print("=" * 50)
        
        note_data = {
            "title": "讨论不倒翁结构",
            "body": "表示不倒翁机械结构需要改善",
            "emotion": 3
        }
        
        print(f"标题: {note_data['title']}")
        print(f"内容: {note_data['body']}")
        print(f"情绪 ID: {note_data['emotion']}")
        
        create_result = await client.notes.create(
            vault_id=vault_id,
            contact_id=contact_id,
            **note_data
        )
        
        if create_result:
            print("\n创建笔记成功:")
            print(json.dumps(create_result, indent=2, ensure_ascii=False))
            
            # 从响应中提取 note_id
            note_id = None
            if isinstance(create_result, dict):
                # 检查响应格式，可能直接是字典或包含 data 字段
                if 'id' in create_result:
                    note_id = str(create_result.get('id', ''))
                elif 'data' in create_result:
                    data = create_result['data']
                    if isinstance(data, dict) and 'id' in data:
                        note_id = str(data.get('id', ''))
            
            if note_id:
                print(f"\n创建的笔记 ID: {note_id}")
                
                # 测试 2: 获取笔记列表
                print("\n" + "=" * 50)
                print("测试 2: 获取笔记列表")
                print("=" * 50)
                
                notes_list = await client.notes.list(
                    vault_id=vault_id,
                    contact_id=contact_id
                )
                
                if notes_list:
                    print(f"\n获取到 {len(notes_list)} 条笔记:")
                    for idx, note in enumerate(notes_list[:5], 1):  # 只显示前5条
                        note_title = note.get('title', 'N/A')
                        note_body = note.get('body', 'N/A')
                        note_id_item = note.get('id', 'N/A')
                        # 截断过长的内容
                        if len(note_body) > 50:
                            note_body = note_body[:50] + "..."
                        print(f"  {idx}. ID: {note_id_item}, 标题: {note_title}, 内容: {note_body}")
                else:
                    print("未获取到笔记（可能 API 返回格式不同）")
                
                # 测试 3: 获取单个笔记（如果列表获取成功）
                if notes_list and len(notes_list) > 0:
                    print("\n" + "=" * 50)
                    print("测试 3: 获取单个笔记")
                    print("=" * 50)
                    
                    first_note_id = notes_list[0].get('id')
                    if first_note_id:
                        get_result = await client.notes.get(
                            vault_id=vault_id,
                            contact_id=contact_id,
                            note_id=str(first_note_id)
                        )
                        
                        if get_result:
                            print("\n获取笔记成功:")
                            print(json.dumps(get_result, indent=2, ensure_ascii=False))
                        else:
                            print("获取笔记失败")
                
                # 测试 4: 更新笔记（如果创建成功）
                print("\n" + "=" * 50)
                print("测试 4: 更新笔记")
                print("=" * 50)
                
                new_body = "表示不倒翁机械结构需要改善\n 更新了下"
                new_emotion = 2
                print(f"新内容: {new_body}")
                print(f"新情绪 ID: {new_emotion}")
                
                update_result = await client.notes.update(
                    vault_id=vault_id,
                    contact_id=contact_id,
                    note_id=note_id,
                    title=note_data['title'],
                    body=new_body,
                    emotion=new_emotion
                )
                
                if update_result:
                    print("\n更新成功:")
                    print(json.dumps(update_result, indent=2, ensure_ascii=False))
                else:
                    print("更新失败")
                
                # 测试 5: 删除笔记（如果更新成功）
                print("\n" + "=" * 50)
                print("测试 5: 删除笔记")
                print("=" * 50)
                
                delete_result = await client.notes.delete(
                    vault_id=vault_id,
                    contact_id=contact_id,
                    note_id=note_id
                )
                
                if delete_result:
                    print("\n删除成功:")
                    print(json.dumps(delete_result, indent=2, ensure_ascii=False))
                else:
                    print("删除失败或已删除")
            else:
                print("\n警告: 无法从响应中提取笔记 ID")
        else:
            print("创建笔记失败")
        
        print("\n" + "=" * 50)
        print("所有测试完成！")
        print("=" * 50)


if __name__ == "__main__":
    asyncio.run(main())

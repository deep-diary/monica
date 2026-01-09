# 创建沟通记录

帮我在@pymonica 这里新增 calls 管理类，实现创建和查询
在@test 目录下新增测试用例

端点 calls

# 通讯协议如下

## Head

Request URL
http://mem.deep-diary.com/vaults/019ba163-d71f-70d0-b3cc-f8a53413f24b/contacts/019ba163-d7a3-72b5-96b5-ba4ea81c0406/calls
Request Method
POST
Status Code
201 Created
Remote Address
127.0.0.1:7890
Referrer Policy
strict-origin-when-cross-origin

## payload

{
"who_initiated": "me",
"called_at": "2026-01-09",
"call_reason_id": 5,
"description": "这里是描述",
"emotion_id": 3,
"type": "audio",
"errors": [],
"isDirty": true,
"hasErrors": false,
"processing": false,
"progress": null,
"wasSuccessful": false,
"recentlySuccessful": false,
"\_\_rememberable": true
}

## responese

{
"who_initiated": "me",
"called_at": "2026-01-09",
"call_reason_id": 5,
"description": "这里是描述",
"emotion_id": 3,
"type": "audio",
"errors": [],
"isDirty": true,
"hasErrors": false,
"processing": false,
"progress": null,
"wasSuccessful": false,
"recentlySuccessful": false,
"\_\_rememberable": true
}

# 更新 call

## Head

Request URL
http://mem.deep-diary.com/vaults/019ba163-d71f-70d0-b3cc-f8a53413f24b/contacts/019ba163-d7a3-72b5-96b5-ba4ea81c0406/calls/5
Request Method
PUT
Status Code
200 OK
Remote Address
127.0.0.1:7890
Referrer Policy
strict-origin-when-cross-origin

## Payload

{
"who_initiated": "contact",
"called_at": "2026-01-09",
"call_reason_id": 5,
"description": "测试 电话通话",
"emotion_id": 3,
"type": "video",
"errors": [],
"isDirty": true,
"hasErrors": false,
"processing": false,
"progress": null,
"wasSuccessful": false,
"recentlySuccessful": false,
"\_\_rememberable": true
}

## Responese

{
"data": {
"id": 5,
"called_at": "1\u6708 09, 2026",
"duration": null,
"description": "\u6d4b\u8bd5 \u7535\u8bdd\u901a\u8bdd",
"who_initiated": "contact",
"type": "video",
"answered": true,
"emotion": {
"id": 3,
"name": "\ud83d\ude01 \u79ef\u6781",
"type": "positive"
},
"reason": {
"id": 5,
"label": "\u6765\u542c\u542c\u4ed6\u4eec\u7684\u6545\u4e8b"
},
"url": {
"update": "http:\/\/mem.deep-diary.com\/vaults\/019ba163-d71f-70d0-b3cc-f8a53413f24b\/contacts\/019ba163-d7a3-72b5-96b5-ba4ea81c0406\/calls\/5",
"destroy": "http:\/\/mem.deep-diary.com\/vaults\/019ba163-d71f-70d0-b3cc-f8a53413f24b\/contacts\/019ba163-d7a3-72b5-96b5-ba4ea81c0406\/calls\/5"
}
}
}

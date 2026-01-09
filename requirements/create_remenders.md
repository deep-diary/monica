# 创建笔记

帮我在@pymonica 这里新增 remenders 管理类，实现创建和查询
在@test 目录下新增测试用例

端点 remenders

# 通讯协议如下

## Head

Request URL
http://mem.deep-diary.com/vaults/019ba163-d71f-70d0-b3cc-f8a53413f24b/contacts/019ba163-d7a3-72b5-96b5-ba4ea81c0406/reminders
Request Method
POST
Status Code
201 Created
Remote Address
112.17.30.188:80
Referrer Policy
strict-origin-when-cross-origin

## payload

{
"label": "test remender",
"reminderChoice": "one_time",
"day": "",
"month": "",
"choice": "full_date",
"date": "2026-01-09",
"frequencyType": "recurring_year",
"frequencyNumber": 1,
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
"data": {
"id": 8,
"label": "test remender",
"date": "1\u6708 09, 2026",
"type": "one_time",
"frequency_number": 1,
"day": 9,
"month": 1,
"choice": "full_date",
"reminder_choice": "one_time",
"url": {
"update": "http:\/\/mem.deep-diary.com\/vaults\/019ba163-d71f-70d0-b3cc-f8a53413f24b\/contacts\/019ba163-d7a3-72b5-96b5-ba4ea81c0406\/reminders\/8",
"destroy": "http:\/\/mem.deep-diary.com\/vaults\/019ba163-d71f-70d0-b3cc-f8a53413f24b\/contacts\/019ba163-d7a3-72b5-96b5-ba4ea81c0406\/reminders\/8"
}
}
}

# 更新 notes

## Head

Request URL
http://mem.deep-diary.com/vaults/019ba163-d71f-70d0-b3cc-f8a53413f24b/contacts/019ba163-d7a3-72b5-96b5-ba4ea81c0406/reminders/8
Request Method
PUT
Status Code
200 OK
Remote Address
112.17.30.188:80
Referrer Policy
strict-origin-when-cross-origin

## Payload

{
"label": "test remender update",
"reminderChoice": "recurring",
"day": 9,
"month": 1,
"choice": "full_date",
"date": "2026-01-10",
"frequencyType": "recurring_year",
"frequencyNumber": 1,
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
"id": 8,
"label": "test remender update",
"date": "1\u6708 10, 2026",
"type": "recurring_year",
"frequency_number": 1,
"day": 10,
"month": 1,
"choice": "full_date",
"reminder_choice": "recurring",
"url": {
"update": "http:\/\/mem.deep-diary.com\/vaults\/019ba163-d71f-70d0-b3cc-f8a53413f24b\/contacts\/019ba163-d7a3-72b5-96b5-ba4ea81c0406\/reminders\/8",
"destroy": "http:\/\/mem.deep-diary.com\/vaults\/019ba163-d71f-70d0-b3cc-f8a53413f24b\/contacts\/019ba163-d7a3-72b5-96b5-ba4ea81c0406\/reminders\/8"
}
}
}

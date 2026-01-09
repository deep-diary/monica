# 添加第二居所地址

## Head

Request URL
http://mem.deep-diary.com/vaults/019b83b0-bd96-700c-bb9a-9bd74f99202f/contacts/019b83b0-be28-707a-8a43-62c91f5e0207/addresses
Request Method
POST
Status Code
201 Created
Remote Address
112.17.30.188:80
Referrer Policy
strict-origin-when-cross-origin

## payload

### address_type_id 枚举量

主页 1
第二居所 2
工作 3
小木屋 4
其他 5

{
"existing_address": false,
"existing_address_id": 0,
"type": "",
"address_type_id": 2,
"is_past_address": false,
"line_1": "周巷镇开发路 68 号绿城惠园 33 栋 303 室",
"line_2": "",
"city": "宁波市",
"province": "浙江省",
"postal_code": "315324",
"country": "中国",
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
"id": 3,
"is_past_address": false,
"line_1": "\u5468\u5df7\u9547\u5f00\u53d1\u8def68\u53f7\u7eff\u57ce\u60e0\u56ed33\u680b303\u5ba4",
"line_2": null,
"city": "\u5b81\u6ce2\u5e02",
"province": "\u6d59\u6c5f\u7701",
"postal_code": "315324",
"country": "\u4e2d\u56fd",
"type": {
"id": 2,
"name": "\ud83c\udfe0 \u7b2c\u4e8c\u5c45\u6240"
},
"url": {
"show": "https:\/\/www.openstreetmap.org\/search?query=%E5%91%A8%E5%B7%B7%E9%95%87%E5%BC%80%E5%8F%91%E8%B7%AF68%E5%8F%B7%E7%BB%BF%E5%9F%8E%E6%83%A0%E5%9B%AD33%E6%A0%8B303%E5%AE%A4+%E5%AE%81%E6%B3%A2%E5%B8%82+%E6%B5%99%E6%B1%9F%E7%9C%81+315324+%E4%B8%AD%E5%9B%BD",
"update": "http:\/\/mem.deep-diary.com\/vaults\/019b83b0-bd96-700c-bb9a-9bd74f99202f\/contacts\/019b83b0-be28-707a-8a43-62c91f5e0207\/addresses\/3",
"destroy": "http:\/\/mem.deep-diary.com\/vaults\/019b83b0-bd96-700c-bb9a-9bd74f99202f\/contacts\/019b83b0-be28-707a-8a43-62c91f5e0207\/addresses\/3"
}
}
}

# 更新地址

## Head

Request URL
http://mem.deep-diary.com/vaults/019ba163-d71f-70d0-b3cc-f8a53413f24b/contacts/019ba163-d7a3-72b5-96b5-ba4ea81c0406/addresses/9
Request Method
PUT
Status Code
200 OK
Remote Address
112.17.30.188:80
Referrer Policy
strict-origin-when-cross-origin

## payload

{
"existing_address": false,
"existing_address_id": 0,
"type": "",
"address_type_id": 1,
"is_past_address": false,
"line_1": "测试地址 主页 修改",
"line_2": null,
"city": "测试城市",
"province": "测试省份",
"postal_code": null,
"country": "中国",
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
"id": 9,
"is_past_address": false,
"line_1": "\u6d4b\u8bd5\u5730\u5740 \u4e3b\u9875 \u4fee\u6539",
"line_2": null,
"city": "\u6d4b\u8bd5\u57ce\u5e02",
"province": "\u6d4b\u8bd5\u7701\u4efd",
"postal_code": null,
"country": "\u4e2d\u56fd",
"type": {
"id": 1,
"name": "\ud83c\udfe1 \u4e3b\u9875"
},
"url": {
"show": "https:\/\/www.openstreetmap.org\/search?query=%E6%B5%8B%E8%AF%95%E5%9C%B0%E5%9D%80+%E4%B8%BB%E9%A1%B5+%E4%BF%AE%E6%94%B9+%E6%B5%8B%E8%AF%95%E5%9F%8E%E5%B8%82+%E6%B5%8B%E8%AF%95%E7%9C%81%E4%BB%BD+%E4%B8%AD%E5%9B%BD",
"update": "http:\/\/mem.deep-diary.com\/vaults\/019ba163-d71f-70d0-b3cc-f8a53413f24b\/contacts\/019ba163-d7a3-72b5-96b5-ba4ea81c0406\/addresses\/9",
"destroy": "http:\/\/mem.deep-diary.com\/vaults\/019ba163-d71f-70d0-b3cc-f8a53413f24b\/contacts\/019ba163-d7a3-72b5-96b5-ba4ea81c0406\/addresses\/9"
}
}
}

# 添加邮箱

## Head

Request URL
http://mem.deep-diary.com/vaults/019b83b0-bd96-700c-bb9a-9bd74f99202f/contacts/019b83b0-be28-707a-8a43-62c91f5e0207/contactInformation
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
"data": "deep-diary@qq.com",
"contact_information_type_id": 1,
"errors": []
}

## responese

{
"data": {
"id": 1,
"label": "deep-diary@qq.com",
"protocol": "mailto:",
"data": "deep-diary@qq.com",
"data_with_protocol": "mailto:deep-diary@qq.com",
"contact_information_type": {
"id": 1,
"name": "\u7535\u5b50\u90ae\u4ef6\u5730\u5740"
},
"url": {
"update": "http:\/\/mem.deep-diary.com\/vaults\/019b83b0-bd96-700c-bb9a-9bd74f99202f\/contacts\/019b83b0-be28-707a-8a43-62c91f5e0207\/contactInformation\/1",
"destroy": "http:\/\/mem.deep-diary.com\/vaults\/019b83b0-bd96-700c-bb9a-9bd74f99202f\/contacts\/019b83b0-be28-707a-8a43-62c91f5e0207\/contactInformation\/1"
}
}
}

# 添加电话

## Head

Request URL
http://mem.deep-diary.com/vaults/019b83b0-bd96-700c-bb9a-9bd74f99202f/contacts/019b83b0-be28-707a-8a43-62c91f5e0207/contactInformation
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
"data": "15055305685",
"contact_information_type_id": 2,
"errors": []
}

## responese

{
"data": {
"id": 2,
"label": "15055305685",
"protocol": "tel:",
"data": "15055305685",
"data_with_protocol": "tel:15055305685",
"contact_information_type": {
"id": 2,
"name": "\u7535\u8bdd"
},
"url": {
"update": "http:\/\/mem.deep-diary.com\/vaults\/019b83b0-bd96-700c-bb9a-9bd74f99202f\/contacts\/019b83b0-be28-707a-8a43-62c91f5e0207\/contactInformation\/2",
"destroy": "http:\/\/mem.deep-diary.com\/vaults\/019b83b0-bd96-700c-bb9a-9bd74f99202f\/contacts\/019b83b0-be28-707a-8a43-62c91f5e0207\/contactInformation\/2"
}
}
}

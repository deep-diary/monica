# 批量创建联系人脚本

## 需求描述
从 contacts.csv 中获取 FirstName, LastName, Gender，创建一个脚本，调用 contact_manager.py，实现批量创建用户。
其中 NickName 使用 pypinyin 实现中文全拼，格式为全小写无空格（便于检索），例如：chencuanxiu

vault_id = "019b83ae-f4bc-7360-bab1-84e226a00e43"  # friends

## 使用方法

### 1. 安装依赖
```bash
pip install pypinyin
```

### 2. 配置环境变量（可选）
```bash
export MONICA_TOKEN="your_monica_token"
export MONICA_BASE_URL="http://your-monica-url.com"
```

如果不设置环境变量，脚本会使用默认值（需要修改脚本中的默认值）。

### 3. 准备 CSV 文件
确保 `contacts.csv` 文件包含以下列：
- FirstName: 名字
- LastName: 姓氏
- Gender: 性别（"男" 或 "女"）

### 4. 运行脚本
```bash
cd scripts
python batch_create_contacts.py
```

## 功能说明

- **自动生成昵称**: 使用 pypinyin 将中文姓名转换为全拼，格式为全小写无空格（便于检索），例如：`machengxue`、`chencuanxiu`
- **性别映射**: 自动将 "男"/"女" 映射到对应的 gender_id
- **智能创建/更新**: 
  - 脚本会先获取 vault 中所有现有联系人
  - 如果联系人已存在（通过姓名匹配），则执行更新操作
  - 如果联系人不存在，则执行创建操作
  - 避免重复创建联系人
- **批量处理**: 自动读取 CSV 文件中的所有联系人并批量处理（创建或更新）
- **错误处理**: 显示每个联系人的处理状态，最后显示新建/更新/失败的统计信息 
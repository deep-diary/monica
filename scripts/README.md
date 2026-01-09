# 批量创建联系人脚本

## 需求描述

从 CSV 文件中获取 FirstName, LastName, Gender，创建一个脚本，调用 contact_manager.py，实现批量创建用户。
其中 NickName 使用 pypinyin 实现中文全拼，格式为全小写无空格（便于检索），例如：chencuanxiu

**注意**: 即使 CSV 文件中包含 NickName 字段，脚本也会自动使用 pypinyin 生成昵称，不会使用 CSV 中的 NickName 值。

## Vault ID 配置

- Friends vault: `019b83ae-f4bc-7360-bab1-84e226a00e43`
- Colleagues vault: `019b83b0-bd96-700c-bb9a-9bd74f99202f`

可以在脚本的 `main()` 函数中修改 `vault_id` 和 `csv_file` 来使用不同的文件和 vault。

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

脚本目录中包含以下 CSV 文件：

- `friends.csv`: 朋友联系人列表
- `colleagues.csv`: 同事联系人列表
- `template.csv`: CSV 文件模板示例

CSV 文件应包含以下列（脚本目前只使用前三个字段）：

- **FirstName**: 名字（必填）
- **LastName**: 姓氏（必填）
- **Gender**: 性别（"男" 或 "女"，可选）
- NickName: 昵称（可选，脚本会忽略此字段，自动生成）
- Email: 邮箱（可选，脚本暂未使用）
- Phone: 电话（可选，脚本暂未使用）
- Address: 地址（可选，脚本暂未使用）
- City: 城市（可选，脚本暂未使用）
- Resource: 资源（可选，脚本暂未使用）
- Need: 需求（可选，脚本暂未使用）

### 4. 运行脚本

```bash
cd scripts
python batch_create_contacts.py
```

## 功能说明

- **自动生成昵称**: 使用 pypinyin 将中文姓名转换为全拼，格式为全小写无空格（便于检索），例如：`machengxue`、`chencuanxiu`
  - **注意**: 即使 CSV 文件中包含 NickName 字段，脚本也会忽略它并自动生成昵称
- **性别映射**: 自动将 "男"/"女" 映射到对应的 gender_id
- **智能创建/更新**:
  - 脚本会先获取 vault 中所有现有联系人
  - 如果联系人已存在（通过姓名或昵称匹配），则执行更新操作
  - 如果联系人不存在，则执行创建操作
  - 避免重复创建联系人
- **批量处理**: 自动读取 CSV 文件中的所有联系人并批量处理（创建或更新）
- **错误处理**: 显示每个联系人的处理状态，最后显示新建/更新/失败的统计信息

## 文件说明

- `friends.csv`: 朋友联系人数据（已格式化，符合标准 CSV 格式）
- `colleagues.csv`: 同事联系人数据（已格式化，符合标准 CSV 格式）
- `template.csv`: CSV 文件格式模板示例

**注意**: `friends.csv` 和 `colleagues.csv` 已在 `.gitignore` 中被忽略，不会被提交到 Git 仓库。

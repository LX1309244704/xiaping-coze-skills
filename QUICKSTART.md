# 飞书多维表格自动化工作流 - 快速开始

## 🚀 快速开始（5分钟搞定）

### 步骤1：创建飞书应用（2分钟）

1. 访问飞书开放平台：https://open.feishu.cn
2. 登录账号
3. 点击"创建企业自建应用"
4. 填写应用信息：
   - 应用名称：虾评技能自动化
   - 应用描述：自动管理虾评技能数据
5. 点击"创建"

### 步骤2：配置应用权限（1分钟）

1. 进入应用详情页
2. 点击左侧"权限管理"
3. 搜索并添加以下权限：
   - `bitable:app`：读取多维表格
   - `bitable:app:readonly`：只读权限
   - `bitable:app:write`：写入权限
4. 点击"申请权限"
5. 在"权限管理"页面，申请权限审核通过

### 步骤3：获取凭证（30秒）

1. 在应用详情页，点击左侧"凭证与基础信息"
2. 复制以下信息：
   - App ID（格式：cli_xxxxxxxxxxxxx）
   - App Secret（格式：xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx）

### 步骤4：配置环境变量（1分钟）

1. 编辑 `.env` 文件：

```bash
cp .env.bitable .env
vi .env  # 或使用你喜欢的编辑器
```

2. 填写配置：

```env
FEISHU_APP_ID=cli_xxxxxxxxxxxxx              # 替换为你的App ID
FEISHU_APP_SECRET=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx  # 替换为你的App Secret
BITABLE_APP_TOKEN=AXDyb30BNamJJ6sMYh2cda7Gnxg    # 保持不变
BITABLE_TABLE_ID=tblWpzyKj1W3juJS             # 保持不变
XIAPING_API_KEY=sk_HjahzeA9nQEnjGmsAklZ1kyaUdnQi8IL  # 保持不变
```

### 步骤5：安装并测试（30秒）

```bash
# 安装依赖
pip3 install -r requirements_bitable.txt

# 测试运行
python3 bitable_automation.py --task=daily_checkin
```

如果看到"每日签到成功"，说明配置正确！🎉

---

## 📋 定时任务说明

自动化工作流会自动执行以下任务：

| 任务 | 执行时间 | 说明 |
|------|---------|------|
| 每日签到 | 17:00 | 自动在虾评平台签到 |
| 收益统计 | 18:00 | 统计今日收益并记录到飞书表格 |
| 客户跟进 | 每6小时 | 检查需要跟进的客户并发送提醒 |
| 新技能评分 | 每10分钟 | 自动计算新技能的综合评分 |

---

## 🔍 查看日志

```bash
# 查看主日志
tail -f /tmp/bitable_automation.log

# 查看签到日志
tail -f /tmp/bitable_automation/checkin.log

# 查看收益统计日志
tail -f /tmp/bitable_automation/revenue.log
```

---

## 🛠️ 管理定时任务

```bash
# 查看当前定时任务
crontab -l

# 编辑定时任务
crontab -e

# 删除所有定时任务
crontab -r
```

---

## 📊 预期效果

配置完成后，你将获得：

✅ **自动化签到**：每天17:00自动在虾评平台签到，获得1-5虾米
✅ **自动收益统计**：每天18:00自动统计收益并记录到飞书表格
✅ **智能技能评分**：每10分钟自动计算新技能的综合评分
✅ **客户跟进提醒**：每6小时自动检查需要跟进的客户

**预期收益**：
- 每日虾米收益：1-5虾米
- 每月虾米收益：30-150虾米
- 效率提升：3-4倍

---

## ❓ 常见问题

### Q1：为什么签到失败？

**A**：请检查：
1. `.env` 文件中的 `XIAPING_API_KEY` 是否正确
2. 是否在签到时间窗口内（09:00-11:00 或 17:00-19:00）
3. 查看日志文件获取详细错误信息

### Q2：为什么无法连接到飞书？

**A**：请检查：
1. `.env` 文件中的 `FEISHU_APP_ID` 和 `FEISHU_APP_SECRET` 是否正确
2. 飞书应用权限是否已审核通过
3. 网络连接是否正常

### Q3：如何修改定时任务时间？

**A**：编辑crontab：
```bash
crontab -e
```
找到对应任务，修改时间格式即可。

### Q4：如何手动执行某个任务？

**A**：使用命令行参数：
```bash
# 只执行签到
python3 bitable_automation.py --task=daily_checkin

# 只执行收益统计
python3 bitable_automation.py --task=daily_revenue

# 只执行新技能评分
python3 bitable_automation.py --task=new_skill

# 只执行客户跟进
python3 bitable_automation.py --task=customer_followup
```

### Q5：如何停止自动化任务？

**A**：删除crontab：
```bash
crontab -r
```

---

## 📞 获取帮助

- **详细文档**：BITABLE_AUTOMATION.md
- **飞书开放平台**：https://open.feishu.cn
- **飞书多维表格文档**：https://open.feishu.cn/document/server-docs/bitable-v1/app-table

---

**快速开始完成！现在你拥有了自动化飞书多维表格管理能力！** 🎉

---

**文档版本**：v1.0
**创建日期**：2026-03-26
**维护人**：三金的小虾米

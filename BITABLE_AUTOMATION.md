# 飞书多维表格自动化工作流配置

## 📋 表格信息

**表格URL**：https://yg72dh0d7x.feishu.cn/base/AXDyb30BNamJJ6sMYh2cda7Gnxg

**App Token**：AXDyb30BNamJJ6sMYh2cda7Gnxg

**Table ID**：tblWpzyKj1W3juJS

---

## 🔄 自动化工作流

### 工作流1：新技能自动评分

**触发条件**：新增技能记录时

**执行逻辑**：
1. 监听表格变更事件
2. 当新增记录时，获取技能信息
3. 根据下载量、评分、商业价值计算综合评分
4. 更新记录的"综合评分"字段

**评分公式**：
```
综合评分 = (下载量权重 × 下载量得分) + (评分权重 × 评分得分) + (商业价值权重 × 商业价值得分)

下载量得分 = min(下载量 / 1000, 10)
评分得分 = 评分 / 10
商业价值得分 = {
  "高": 10,
  "中": 7,
  "低": 4
}

权重配置：
- 下载量权重：0.4
- 评分权重：0.4
- 商业价值权重：0.2
```

**Python实现**：
```python
def calculate_score(download_count: int, rating: float, commercial_value: str) -> float:
    """计算综合评分"""
    # 归一化得分
    download_score = min(download_count / 1000, 10)
    rating_score = rating / 10
    commercial_score = {"高": 10, "中": 7, "低": 4}.get(commercial_value, 5)

    # 加权计算
    final_score = (
        0.4 * download_score +
        0.4 * rating_score +
        0.2 * commercial_score
    )

    return round(final_score, 2)
```

---

### 工作流2：每日收益统计

**触发时间**：每日18:00

**执行逻辑**：
1. 获取虾评今日收益
2. 获取扣子今日收益
3. 计算总收益和ROI
4. 创建新的收益记录

**记录字段**：
- 日期（日期）
- 虾评收益（数字）
- 扣子收益（数字）
- 总收益（公式：虾评收益 + 扣子收益）
- ROI（数字）
- 统计时间（创建时间）

**Python实现**：
```python
def daily_revenue_stats():
    """每日收益统计"""
    # 获取虾评收益
    xiaping_revenue = get_xiaping_daily_revenue()

    # 获取扣子收益
    coze_revenue = get_coze_daily_revenue()

    # 计算总收益
    total_revenue = xiaping_revenue + coze_revenue

    # 创建记录
    fields = {
        "日期": datetime.now().strftime("%Y-%m-%d"),
        "虾评收益": xiaping_revenue,
        "扣子收益": coze_revenue,
        "总收益": total_revenue,
        "ROI": calculate_roi(total_revenue),
        "统计时间": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    return create_bitable_record(fields)
```

---

### 工作流3：客户跟进提醒

**触发条件**：
- 新客户添加时
- 跟进时间到期时

**执行逻辑**：
1. 检查客户表
2. 识别需要跟进的客户
3. 发送飞书消息提醒
4. 更新跟进状态

**提醒规则**：
- 新客户：添加后24小时内提醒
- 跟进中客户：每3天提醒一次
- 成交客户：签约后30天提醒满意度调研

**Python实现**：
```python
def customer_followup_reminder():
    """客户跟进提醒"""
    # 获取需要跟进的客户
    customers = get_customers_need_followup()

    # 发送提醒
    for customer in customers:
        message = f"📢 客户跟进提醒\n\n客户：{customer['name']}\n需求：{customer['requirement']}\n跟进时间：{customer['followup_time']}\n备注：{customer.get('remark', '无')}"

        # 发送飞书消息
        send_feishu_message(message)

        # 更新跟进状态
        update_followup_status(customer['id'], "已提醒")
```

---

## 🛠️ 实现步骤

### 步骤1：创建飞书应用

1. 访问飞书开放平台：https://open.feishu.cn
2. 创建企业自建应用
3. 配置权限：
   - `bitable:app`：读取多维表格
   - `bitable:app:readonly`：只读权限
   - `bitable:app:write`：写入权限
4. 获取App ID和App Secret

### 步骤2：配置环境变量

```bash
# .env 文件
FEISHU_APP_ID=cli_xxxxxxxxxxxxx
FEISHU_APP_SECRET=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
BITABLE_APP_TOKEN=AXDyb30BNamJJ6sMYh2cda7Gnxg
BITABLE_TABLE_ID=tblWpzyKj1W3juJS
```

### 步骤3：安装依赖

```bash
pip install requests lark-oapi
```

### 步骤4：创建自动化脚本

创建 `bitable_automation.py` 文件，包含所有自动化工作流的实现。

### 步骤5：配置定时任务

```bash
# 编辑 crontab
crontab -e

# 添加以下内容：
# 每日18:00执行收益统计
0 18 * * * /usr/bin/python3 /path/to/bitable_automation.py --task=daily_revenue

# 每6小时检查客户跟进
0 */6 * * * /usr/bin/python3 /path/to/bitable_automation.py --task=customer_followup

# 每10分钟检查新技能
*/10 * * * * /usr/bin/python3 /path/to/bitable_automation.py --task=new_skill_score
```

---

## 📊 数据表设计

### 收益分析表（Bitable）

**字段配置**：
| 字段名称 | 字段类型 | 说明 | 默认值 |
|---------|---------|------|--------|
| 日期 | 日期 | 统计日期 | - |
| 虾评收益 | 数字 | 虾评平台收益（虾米） | 0 |
| 扣子收益 | 数字 | 扣子平台收益（元） | 0 |
| 总收益 | 数字 | 总收益（公式） | 0 |
| ROI | 数字 | 投资回报率 | 0% |
| 统计时间 | 创建时间 | 统计时间戳 | 自动生成 |

### 客户管理表（Bitable）

**字段配置**：
| 字段名称 | 字段类型 | 说明 | 默认值 |
|---------|---------|------|--------|
| 客户名称 | 文本 | 客户姓名/公司名 | - |
| 联系方式 | 电话 | 联系电话 | - |
| 需求描述 | 文本 | 客户需求描述 | - |
| 项目进度 | 单选 | 待跟进/跟进中/已成交/已关闭 | 待跟进 |
| 合同金额 | 货币 | 合同金额 | ¥0 |
| 付款状态 | 单选 | 未付款/部分付款/已付款 | 未付款 |
| 跟进时间 | 日期 | 下次跟进时间 | - |
| 备注 | 文本 | 备注信息 | - |

### 任务管理表（Bitable）

**字段配置**：
| 字段名称 | 字段类型 | 说明 | 默认值 |
|---------|---------|------|--------|
| 任务名称 | 文本 | 任务名称 | - |
| 任务类型 | 单选 | 虾评任务/扣子任务/飞书任务/其他 | - |
| 优先级 | 单选 | 高/中/低 | 中 |
| 负责人 | 人员 | 任务负责人 | - |
| 截止日期 | 日期 | 任务截止时间 | - |
| 完成状态 | 单选 | 待开始/进行中/已完成/已关闭 | 待开始 |
| 备注 | 文本 | 任务备注 | - |

---

## 🔧 飞书API调用示例

### 获取表格记录

```python
import lark_oapi as lark
from lark_oapi.api.bitable.v1 import *

def get_bitable_records(app_token: str, table_id: str, filter_dict: dict = None) -> dict:
    """获取表格记录"""
    # 构建client
    client = lark.Client.builder() \
        .app_id(os.getenv("FEISHU_APP_ID")) \
        .app_secret(os.getenv("FEISHU_APP_SECRET")) \
        .build()

    # 构建请求
    request = ListAppTableRecordRequest.builder() \
        .app_token(app_token) \
        .table_id(table_id) \
        .filter(json.dumps(filter_dict) if filter_dict else None) \
        .build()

    # 发送请求
    response = client.bitable.v1.app_table_record.list(request)

    if not response.success():
        print(f"请求失败: {response.code} - {response.msg}")
        return None

    return response.data
```

### 创建记录

```python
def create_bitable_record(app_token: str, table_id: str, fields: dict) -> dict:
    """创建记录"""
    # 构建client
    client = lark.Client.builder() \
        .app_id(os.getenv("FEISHU_APP_ID")) \
        .app_secret(os.getenv("FEISHU_APP_SECRET")) \
        .build()

    # 构建请求
    request = CreateAppTableRecordRequest.builder() \
        .app_token(app_token) \
        .table_id(table_id) \
        .fields(fields) \
        .build()

    # 发送请求
    response = client.bitable.v1.app_table_record.create(request)

    if not response.success():
        print(f"请求失败: {response.code} - {response.msg}")
        return None

    return response.data
```

### 更新记录

```python
def update_bitable_record(app_token: str, table_id: str, record_id: str, fields: dict) -> dict:
    """更新记录"""
    # 构建client
    client = lark.Client.builder() \
        .app_id(os.getenv("FEISHU_APP_ID")) \
        .app_secret(os.getenv("FEISHU_APP_SECRET")) \
        .build()

    # 构建请求
    request = UpdateAppTableRecordRequest.builder() \
        .app_token(app_token) \
        .table_id(table_id) \
        .record_id(record_id) \
        .fields(fields) \
        .build()

    # 发送请求
    response = client.bitable.v1.app_table_record.update(request)

    if not response.success():
        print(f"请求失败: {response.code} - {response.msg}")
        return None

    return response.data
```

---

## 📈 监控与日志

### 日志记录

```python
import logging

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('/var/log/bitable_automation.log'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

# 使用日志
logger.info("自动化工作流开始执行")
logger.error("执行失败: %s", error_message)
logger.info("自动化工作流执行完成")
```

### 性能监控

```python
import time

def monitor_performance(func):
    """性能监控装饰器"""
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()

        execution_time = end_time - start_time
        logger.info(f"{func.__name__} 执行时间: {execution_time:.2f}秒")

        return result
    return wrapper

@monitor_performance
def daily_revenue_stats():
    """每日收益统计（带性能监控）"""
    # 实现代码
    pass
```

---

## 🎯 预期效果

### 效率提升
- **数据录入**：自动化录入，减少90%手动工作
- **数据更新**：实时更新，减少80%等待时间
- **数据分析**：自动分析，减少70%分析时间
- **流程优化**：自动化流程，提升3-4倍整体效率

### 管理提升
- **实时监控**：数据实时更新，决策更及时
- **自动提醒**：关键节点自动提醒，避免遗漏
- **智能分析**：自动生成分析报告，洞察更深入
- **标准化流程**：统一流程，降低人为错误

---

## 📝 维护指南

### 日常维护
1. 每日检查日志文件，确认自动化任务正常执行
2. 每周检查数据准确性，确保无异常数据
3. 每月检查飞书API调用额度，确保不超限
4. 每季度优化自动化逻辑，提升效率

### 故障处理
1. 查看日志文件，定位故障原因
2. 检查网络连接，确认API调用正常
3. 检查飞书应用配置，确认权限正确
4. 检查定时任务配置，确认cron服务正常

---

## 📞 技术支持

- **飞书开放平台**：https://open.feishu.cn
- **飞书多维表格文档**：https://open.feishu.cn/document/server-docs/bitable-v1/app-table
- **Lark SDK文档**：https://github.com/larksuite/oapi-sdk-python

---

**文档版本**：v1.0
**创建日期**：2026-03-26
**维护人**：三金的小虾米

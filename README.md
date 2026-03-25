# 🦞 虾评扣子技能整合平台 - 三金的小虾米出品

**整合虾评平台TOP5热门技能 + 扣子平台TOP5热门技能，一站式AI技能集成平台！**

> 汇聚全网最热门的AI技能，让你的AI智能体瞬间变身专家！

---

## ✨ 项目简介

**虾评扣子技能整合平台** 是一个整合了虾评和扣子平台热门技能的开源项目，提供：

### 📊 虾评平台TOP5热门技能
1. 🔍 **百度搜索Skill** - 下载量3.6万+，全球第一
2. 🎓 **学术民工虾** - 学术研究辅助
3. 🌐 **百度龙虾全家桶** - 多种搜索技能
4. 📚 **腾讯云SkillHub** - 13000+技能
5. 🏪 **技能仓库** - 2.3万人收藏

### 🤖 扣子平台TOP5热门技能
1. 💰 **财务分析技能** - 专业数据分析
2. 📊 **PPT生成技能** - 自动化文档
3. 📈 **市场分析技能** - 智能分析
4. 🔒 **私有技能** - 个性化定制
5. 🎯 **工作流编排** - 流程自动化

---

## 🎯 核心技能模块

### 第1部分：虾评热门技能

#### 1. 百度搜索Skill（下载量3.6万+）
```python
from skills.xiaping.baidu_search import BaiduSearch

search = BaiduSearch()
results = search.search("OpenClaw技能", num_results=10)
```

**功能特点**：
- 全球下载量第一
- 智能搜索优化
- 多语言支持
- 搜索结果聚合

#### 2. 学术民工虾
```python
from skills.xiaping.academic_assistant import AcademicAssistant

assistant = AcademicAssistant()
paper = assistant.generate_paper("AI Agent架构设计")
```

**功能特点**：
- 学术论文生成
- 文献检索
- 数据分析
- 图表生成

#### 3. 百度龙虾全家桶
```python
from skills.xiaping.baidu_family import BaiduFamilyBucket

bucket = BaiduFamilyBucket()
results = bucket.search_all("AI技术")
```

**功能特点**：
- 多平台搜索
- 深度检索
- 结果去重
- 智能排序

#### 4. 腾讯云SkillHub
```python
from skills.xiaping.tencent_skillhub import TencentSkillHub

hub = TencentSkillHub()
skills = hub.search_skills("数据处理")
```

**功能特点**：
- 13000+技能
- 技能分类管理
- 安全审计
- 一键安装

#### 5. 技能仓库
```python
from skills.xiaping.skill_repo import SkillRepository

repo = SkillRepository()
popular = repo.get_popular_skills(limit=20)
```

**功能特点**：
- 2.3万人收藏
- 技能榜单
- 评分系统
- 使用统计

---

### 第2部分：扣子热门技能

#### 1. 财务分析技能
```python
from skills.coze.finance_analysis import FinanceAnalysis

finance = FinanceAnalysis()
report = finance.analyze_stock("阿里巴巴", period="Q1")
```

**功能特点**：
- 股票数据分析
- 财务报表生成
- 投资建议
- 风险评估

#### 2. PPT生成技能
```python
from skills.coze.ppt_generator import PPTGenerator

ppt = PPTGenerator()
slides = ppt.generate("AI技术发展趋势", style="modern")
```

**功能特点**：
- 智能内容生成
- 自动排版
- 多模板支持
- 动画效果

#### 3. 市场分析技能
```python
from skills.coze.market_analysis import MarketAnalysis

market = MarketAnalysis()
trends = market.analyze_trends("新能源", period="2024Q1")
```

**功能特点**：
- 市场趋势分析
- 竞品分析
- 用户画像
- 数据可视化

#### 4. 私有技能
```python
from skills.coze.private_skill import PrivateSkill

skill = PrivateSkill()
workflow = skill.create_workflow("我的专属流程")
```

**功能特点**：
- 个性化定制
- 流程自动化
- 数据加密
- 权限管理

#### 5. 工作流编排
```python
from skills.coze.workflow_orchestrator import WorkflowOrchestrator

orchestrator = WorkflowOrchestrator()
result = orchestrator.execute("数据分析流程")
```

**功能特点**：
- 多步骤编排
- 条件判断
- 异步执行
- 错误处理

---

## 🚀 快速开始

### 环境要求
- Python 3.9+
- Node.js 18+
- OpenClaw环境
- 扣子账号

### 安装部署

```bash
# 克隆仓库
git clone https://github.com/LX1309244704/xiaping-coze-skills.git
cd xiaping-coze-skills

# 安装Python依赖
pip install -r requirements.txt

# 配置环境变量
cp .env.example .env
# 编辑 .env 文件

# 启动服务
python main.py
```

### 快速使用示例

#### 虾评技能使用
```python
# 百度搜索
from skills.xiaping.baidu_search import BaiduSearch

search = BaiduSearch()
results = search.search("AI Agent")

# 学术民工虾
from skills.xiaping.academic_assistant import AcademicAssistant

assistant = AcademicAssistant()
paper = assistant.generate_paper("深度学习")

# 技能仓库
from skills.xiaping.skill_repo import SkillRepository

repo = SkillRepository()
popular = repo.get_popular_skills()
```

#### 扣子技能使用
```python
# 财务分析
from skills.coze.finance_analysis import FinanceAnalysis

finance = FinanceAnalysis()
report = finance.analyze_company("腾讯")

# PPT生成
from skills.coze.ppt_generator import PPTGenerator

ppt = PPTGenerator()
slides = ppt.generate("产品介绍", template="business")

# 工作流编排
from skills.coze.workflow_orchestrator import WorkflowOrchestrator

orchestrator = WorkflowOrchestrator()
result = orchestrator.execute("自动化流程")
```

---

## 📊 项目结构

```
xiaping-coze-skills/
├── skills/
│   ├── xiaping/              # 虾评热门技能
│   │   ├── baidu_search.py   # 百度搜索
│   │   ├── academic_assistant.py # 学术民工虾
│   │   ├── baidu_family.py  # 百度龙虾全家桶
│   │   ├── tencent_skillhub.py # 腾讯云SkillHub
│   │   └── skill_repo.py     # 技能仓库
│   ├── coze/                 # 扣子热门技能
│   │   ├── finance_analysis.py # 财务分析
│   │   ├── ppt_generator.py  # PPT生成
│   │   ├── market_analysis.py # 市场分析
│   │   ├── private_skill.py  # 私有技能
│   │   └── workflow_orchestrator.py # 工作流编排
├── config/
│   ├── settings.py
│   └── constants.py
├── examples/                 # 使用示例
│   ├── xiaping_examples.py
│   ├── coze_examples.py
│   └── integration_examples.py
├── docs/                     # 文档
│   ├── xiaping_skills.md
│   ├── coze_skills.md
│   └── integration_guide.md
├── tests/                    # 测试
│   ├── test_xiaping.py
│   ├── test_coze.py
│   └── test_integration.py
├── main.py                   # 主程序
├── requirements.txt
├── .env.example
└── README.md
```

---

## 📈 技能数据对比

### 虾评平台技能热度排行

| 排名 | 技能名称 | 下载量 | 特点 |
|------|---------|--------|------|
| 1 | 百度搜索Skill | 3.6万+ | 全球第一 |
| 2 | 技能仓库 | 2.3万收藏 | 2.3万人收藏 |
| 3 | 腾讯云SkillHub | 13000+ | 13000+技能 |
| 4 | 百度龙虾全家桶 | 高 | 多平台搜索 |
| 5 | 学术民工虾 | 高 | 学术研究 |

### 扣子平台技能使用排行

| 排名 | 技能名称 | 使用量 | 特点 |
|------|---------|--------|------|
| 1 | 财务分析技能 | 高 | 专业数据分析 |
| 2 | PPT生成技能 | 高 | 自动化文档 |
| 3 | 市场分析技能 | 高 | 智能分析 |
| 4 | 私有技能 | 中 | 个性化定制 |
| 5 | 工作流编排 | 高 | 流程自动化 |

---

## 🎯 整合优势

### 1. 一站式平台
- 虾评+扣子双平台技能整合
- 统一的API接口
- 一致的使用体验

### 2. 智能选择
- 自动选择最优技能
- 性能对比
- 成本优化

### 3. 无缝切换
- 平台之间自由切换
- 数据共享
- 结果聚合

### 4. 扩展性强
- 模块化设计
- 插件架构
- 易于扩展

---

## 💡 使用场景

### 1. 学术研究
- 文献检索（学术民工虾）
- 论文生成（学术民工虾）
- 数据分析（财务分析）

### 2. 商业分析
- 市场趋势（市场分析）
- 竞品分析（市场分析）
- 财务分析（财务分析）

### 3. 文档处理
- PPT生成（PPT生成）
- 报告生成（工作流编排）
- 数据可视化（数据分析）

### 4. 信息搜索
- 网络搜索（百度搜索）
- 深度检索（百度龙虾全家桶）
- 技能发现（技能仓库）

---

## 📞 联系方式

- **作者**：三金的小虾米
- **邮箱**：1309244704@qq.com
- **GitHub**：https://github.com/LX1309244704/xiaping-coze-skills
- **虾评**：https://xiaping.coze.site

---

## 📄 许可证

MIT License

Copyright (c) 2026 三金的小虾米

---

**🦞 汇聚全网热门技能，让你的AI智能体瞬间变身专家！**

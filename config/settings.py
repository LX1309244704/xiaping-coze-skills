# 项目配置

PROJECT_NAME = "虾评扣子技能整合平台"
VERSION = "1.0.0"
AUTHOR = "三金的小虾米"
EMAIL = "1309244704@qq.com"

# 虾评技能配置
XIAPING_SKILLS = {
    "baidu_search": {
        "name": "百度搜索Skill",
        "downloads": "36,000+",
        "rank": "全球第一",
        "platform": "虾评"
    },
    "academic_assistant": {
        "name": "学术民工虾",
        "platform": "虾评",
        "downloads": "高"
    }
}

# 扣子技能配置
COZE_SKILLS = {
    "finance_analysis": {
        "name": "财务分析技能",
        "platform": "扣子",
        "usage": "高"
    },
    "ppt_generator": {
        "name": "PPT生成技能",
        "platform": "扣子",
        "usage": "高"
    },
    "workflow_orchestrator": {
        "name": "工作流编排",
        "platform": "扣子",
        "usage": "高"
    }
}

# API配置
API_CONFIG = {
    "baidu": {
        "base_url": "https://www.baidu.com",
        "timeout": 30
    },
    "xiaping": {
        "base_url": "https://xiaping.coze.site",
        "timeout": 30
    },
    "coze": {
        "base_url": "https://api.coze.cn",
        "timeout": 30
    }
}

# 日志配置
LOG_CONFIG = {
    "level": "INFO",
    "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    "file": "app.log"
}

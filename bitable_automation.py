#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
飞书多维表格自动化工作流
功能：
1. 新技能自动评分
2. 每日收益统计
3. 客户跟进提醒
"""

import os
import sys
import json
import logging
import argparse
from datetime import datetime, timedelta
from typing import Dict, List, Optional
import requests
import lark_oapi as lark
from lark_oapi.api.bitable.v1 import *

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('/tmp/bitable_automation.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# 环境变量
FEISHU_APP_ID = os.getenv("FEISHU_APP_ID", "")
FEISHU_APP_SECRET = os.getenv("FEISHU_APP_SECRET", "")
BITABLE_APP_TOKEN = os.getenv("BITABLE_APP_TOKEN", "AXDyb30BNamJJ6sMYh2cda7Gnxg")
BITABLE_TABLE_ID = os.getenv("BITABLE_TABLE_ID", "tblWpzyKj1W3juJS")
XIAPING_API_KEY = os.getenv("XIAPING_API_KEY", "sk_HjahzeA9nQEnjGmsAklZ1kyaUdnQi8IL")


class BitableAutomation:
    """飞书多维表格自动化类"""

    def __init__(self):
        """初始化客户端"""
        try:
            self.client = lark.Client.builder() \
                .app_id(FEISHU_APP_ID) \
                .app_secret(FEISHU_APP_SECRET) \
                .build()
            logger.info("飞书客户端初始化成功")
        except Exception as e:
            logger.error(f"飞书客户端初始化失败: {e}")
            self.client = None

    def get_bitable_records(
        self,
        app_token: str,
        table_id: str,
        filter_dict: Optional[Dict] = None
    ) -> Optional[Dict]:
        """获取表格记录"""
        if not self.client:
            logger.error("飞书客户端未初始化")
            return None

        try:
            request = ListAppTableRecordRequest.builder() \
                .app_token(app_token) \
                .table_id(table_id) \
                .filter(json.dumps(filter_dict) if filter_dict else None) \
                .build()

            response = self.client.bitable.v1.app_table_record.list(request)

            if not response.success():
                logger.error(f"获取记录失败: {response.code} - {response.msg}")
                return None

            return response.data

        except Exception as e:
            logger.error(f"获取记录异常: {e}")
            return None

    def create_bitable_record(
        self,
        app_token: str,
        table_id: str,
        fields: Dict
    ) -> Optional[Dict]:
        """创建记录"""
        if not self.client:
            logger.error("飞书客户端未初始化")
            return None

        try:
            request = CreateAppTableRecordRequest.builder() \
                .app_token(app_token) \
                .table_id(table_id) \
                .fields(fields) \
                .build()

            response = self.client.bitable.v1.app_table_record.create(request)

            if not response.success():
                logger.error(f"创建记录失败: {response.code} - {response.msg}")
                return None

            logger.info(f"创建记录成功: {response.data.record.record_id}")
            return response.data

        except Exception as e:
            logger.error(f"创建记录异常: {e}")
            return None

    def update_bitable_record(
        self,
        app_token: str,
        table_id: str,
        record_id: str,
        fields: Dict
    ) -> Optional[Dict]:
        """更新记录"""
        if not self.client:
            logger.error("飞书客户端未初始化")
            return None

        try:
            request = UpdateAppTableRecordRequest.builder() \
                .app_token(app_token) \
                .table_id(table_id) \
                .record_id(record_id) \
                .fields(fields) \
                .build()

            response = self.client.bitable.v1.app_table_record.update(request)

            if not response.success():
                logger.error(f"更新记录失败: {response.code} - {response.msg}")
                return None

            logger.info(f"更新记录成功: {record_id}")
            return response.data

        except Exception as e:
            logger.error(f"更新记录异常: {e}")
            return None


class XiapingAPI:
    """虾评API类"""

    def __init__(self, api_key: str):
        """初始化虾评API"""
        self.api_key = api_key
        self.base_url = "https://xiaping.coze.site/api"

    def checkin(self) -> Dict:
        """签到"""
        try:
            response = requests.post(
                f"{self.base_url}/tasks/checkin",
                headers={"Authorization": f"Bearer {self.api_key}"},
                timeout=10
            )
            return response.json()
        except Exception as e:
            logger.error(f"签到失败: {e}")
            return {"success": False, "error": str(e)}

    def get_daily_revenue(self) -> int:
        """获取今日收益"""
        # 模拟获取今日收益
        # 实际需要调用虾评API获取
        return 10  # 假设今日收益10虾米


def calculate_skill_score(
    download_count: int,
    rating: float,
    commercial_value: str
) -> float:
    """计算技能综合评分"""
    try:
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

    except Exception as e:
        logger.error(f"计算评分失败: {e}")
        return 0.0


def new_skill_score_automation(automation: BitableAutomation) -> bool:
    """新技能自动评分"""
    logger.info("开始执行新技能自动评分")

    try:
        # 获取所有技能记录
        data = automation.get_bitable_records(
            BITABLE_APP_TOKEN,
            BITABLE_TABLE_ID
        )

        if not data or not data.get("items"):
            logger.warning("没有找到技能记录")
            return False

        # 处理每条记录
        for item in data["items"]:
            fields = item.get("fields", {})

            # 获取技能信息
            download_count = fields.get("下载量", 0)
            rating = fields.get("评分", 0)
            commercial_value = fields.get("商业价值", "中")

            # 计算综合评分
            final_score = calculate_skill_score(download_count, rating, commercial_value)

            # 更新记录
            automation.update_bitable_record(
                BITABLE_APP_TOKEN,
                BITABLE_TABLE_ID,
                item.record_id,
                {"综合评分": final_score}
            )

        logger.info(f"新技能自动评分完成，共处理 {len(data['items'])} 条记录")
        return True

    except Exception as e:
        logger.error(f"新技能自动评分失败: {e}")
        return False


def daily_revenue_automation(automation: BitableAutomation) -> bool:
    """每日收益统计"""
    logger.info("开始执行每日收益统计")

    try:
        # 获取虾评收益
        xiaping_api = XiapingAPI(XIAPING_API_KEY)
        xiaping_revenue = xiaping_api.get_daily_revenue()

        # 获取扣子收益（模拟）
        coze_revenue = 0  # 暂时没有扣子收益

        # 计算总收益
        total_revenue = xiaping_revenue + coze_revenue

        # 计算ROI（简单模拟）
        roi = (total_revenue / 100) * 100  # 假设成本为100虾米

        # 创建收益记录
        fields = {
            "日期": datetime.now().strftime("%Y-%m-%d"),
            "虾评收益": xiaping_revenue,
            "扣子收益": coze_revenue,
            "总收益": total_revenue,
            "ROI": round(roi, 2)
        }

        success = automation.create_bitable_record(
            BITABLE_APP_TOKEN,
            BITABLE_TABLE_ID,
            fields
        )

        if success:
            logger.info(f"每日收益统计完成，今日收益: {total_revenue}虾米")
            return True
        else:
            logger.error("创建收益记录失败")
            return False

    except Exception as e:
        logger.error(f"每日收益统计失败: {e}")
        return False


def customer_followup_automation(automation: BitableAutomation) -> bool:
    """客户跟进提醒"""
    logger.info("开始执行客户跟进提醒")

    try:
        # 获取需要跟进的客户（模拟）
        # 实际需要查询客户管理表
        logger.info("客户跟进提醒功能待实现（需要客户管理表）")

        # TODO: 实现客户跟进提醒逻辑
        # 1. 查询需要跟进的客户
        # 2. 发送飞书消息提醒
        # 3. 更新跟进状态

        return True

    except Exception as e:
        logger.error(f"客户跟进提醒失败: {e}")
        return False


def daily_checkin_automation(xiaping_api: XiapingAPI) -> bool:
    """每日签到"""
    logger.info("开始执行每日签到")

    try:
        result = xiaping_api.checkin()

        if result.get("success"):
            logger.info("每日签到成功")
            return True
        else:
            logger.error(f"每日签到失败: {result.get('error')}")
            return False

    except Exception as e:
        logger.error(f"每日签到异常: {e}")
        return False


def main():
    """主函数"""
    parser = argparse.ArgumentParser(description="飞书多维表格自动化工作流")
    parser.add_argument(
        "--task",
        type=str,
        choices=["new_skill", "daily_revenue", "customer_followup", "daily_checkin", "all"],
        default="all",
        help="指定要执行的任务"
    )

    args = parser.parse_args()

    # 初始化自动化类
    automation = BitableAutomation()
    xiaping_api = XiapingAPI(XIAPING_API_KEY)

    # 执行任务
    success = True

    if args.task in ["new_skill", "all"]:
        success &= new_skill_score_automation(automation)

    if args.task in ["daily_revenue", "all"]:
        success &= daily_revenue_automation(automation)

    if args.task in ["customer_followup", "all"]:
        success &= customer_followup_automation(automation)

    if args.task in ["daily_checkin", "all"]:
        success &= daily_checkin_automation(xiaping_api)

    # 返回结果
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()

#!/bin/bash
# 飞书多维表格自动化工作流安装脚本

set -e

echo "🦞 飞书多维表格自动化工作流安装脚本"
echo "===================================="

# 检查Python版本
echo "📋 检查Python版本..."
python_version=$(python3 --version 2>&1 | awk '{print $2}')
echo "Python版本: $python_version"

if [[ $(echo "$python_version" | cut -d. -f1) -lt 3 ]]; then
    echo "❌ Python版本过低，需要Python 3.7或更高版本"
    exit 1
fi

# 安装依赖
echo ""
echo "📦 安装Python依赖..."
pip3 install -r requirements_bitable.txt

# 配置环境变量
echo ""
echo "⚙️  配置环境变量..."
if [ ! -f .env ]; then
    cp .env.bitable .env
    echo "✅ 已创建.env文件，请编辑并填写正确的配置"
    echo "📝 请编辑 .env 文件，填写以下配置："
    echo "   - FEISHU_APP_ID"
    echo "   - FEISHU_APP_SECRET"
    echo "   - BITABLE_APP_TOKEN"
    echo "   - BITABLE_TABLE_ID"
    echo "   - XIAPING_API_KEY"
else
    echo "✅ .env文件已存在"
fi

# 创建日志目录
echo ""
echo "📁 创建日志目录..."
mkdir -p /tmp/bitable_automation
chmod 755 /tmp/bitable_automation

# 配置crontab
echo ""
echo "⏰ 配置定时任务..."
CRON_FILE="/tmp/bitable_crontab.tmp"

# 生成crontab配置
cat > $CRON_FILE << EOF
# 飞书多维表格自动化工作流定时任务

# 每日17:00执行签到
0 17 * * * cd $(pwd) && /usr/bin/python3 $(pwd)/bitable_automation.py --task=daily_checkin >> /tmp/bitable_automation/checkin.log 2>&1

# 每日18:00执行收益统计
0 18 * * * cd $(pwd) && /usr/bin/python3 $(pwd)/bitable_automation.py --task=daily_revenue >> /tmp/bitable_automation/revenue.log 2>&1

# 每6小时检查客户跟进
0 */6 * * * cd $(pwd) && /usr/bin/python3 $(pwd)/bitable_automation.py --task=customer_followup >> /tmp/bitable_automation/followup.log 2>&1

# 每10分钟检查新技能
*/10 * * * * cd $(pwd) && /usr/bin/python3 $(pwd)/bitable_automation.py --task=new_skill >> /tmp/bitable_automation/skill.log 2>&1
EOF

# 安装crontab
echo "当前crontab配置："
crontab -l 2>/dev/null || true

echo ""
echo "是否安装定时任务到crontab？(y/n)"
read -r install_cron

if [[ $install_cron =~ ^[Yy]$ ]]; then
    # 合并crontab
    (crontab -l 2>/dev/null | grep -v "bitable_automation"; cat $CRON_FILE) | crontab -
    echo "✅ 定时任务已安装到crontab"
else
    echo "⏭️  跳过安装定时任务"
    echo "📝 你可以手动编辑crontab，添加以下内容："
    cat $CRON_FILE
fi

# 清理临时文件
rm -f $CRON_FILE

# 测试运行
echo ""
echo "🧪 测试运行..."
if [ -f .env ]; then
    export $(cat .env | xargs)
    python3 bitable_automation.py --task=daily_checkin
    echo "✅ 测试运行成功"
else
    echo "⚠️  请先配置.env文件后运行测试"
fi

# 完成
echo ""
echo "✅ 安装完成！"
echo ""
echo "📋 下一步："
echo "1. 编辑 .env 文件，填写正确的配置"
echo "2. 运行测试: python3 bitable_automation.py --task=daily_checkin"
echo "3. 查看日志: tail -f /tmp/bitable_automation.log"
echo "4. 管理定时任务: crontab -l"
echo ""
echo "📚 文档位置: BITABLE_AUTOMATION.md"
echo ""

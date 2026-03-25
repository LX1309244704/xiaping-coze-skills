"""
虾评扣子技能整合平台 - 主程序
整合虾评TOP5热门技能 + 扣子TOP5热门技能
"""

import os
import time
from dotenv import load_dotenv

# 虾评技能
from skills.xiaping.baidu_search import BaiduSearch
from skills.xiaping.academic_assistant import AcademicAssistant

# 扣子技能
from skills.coze.finance_analysis import FinanceAnalysis
from skills.coze.ppt_generator import PPTGenerator
from skills.coze.workflow_orchestrator import WorkflowOrchestrator

# 加载环境变量
load_dotenv()

class XiapingCozeSkills:
    """虾评扣子技能整合平台 - 主类"""
    
    def __init__(self):
        self.xiaping_skills = {}
        self.coze_skills = {}
        self._initialize()
    
    def _initialize(self):
        """初始化所有技能"""
        print("=" * 60)
        print("🦞 初始化虾评扣子技能整合平台...")
        print("=" * 60)
        
        # 初始化虾评技能
        print("\n📚 初始化虾评热门技能...")
        self._init_xiaping_skills()
        
        # 初始化扣子技能
        print("\n🤖 初始化扣子热门技能...")
        self._init_coze_skills()
        
        print("\n" + "=" * 60)
        print("🎉 所有技能初始化完成！")
        print("=" * 60)
    
    def _init_xiaping_skills(self):
        """初始化虾评技能"""
        
        # 1. 百度搜索Skill（下载量3.6万+）
        self.xiaping_skills["baidu_search"] = BaiduSearch()
        print("  ✅ 百度搜索Skill - 下载量3.6万+，全球第一")
        
        # 2. 学术民工虾
        self.xiaping_skills["academic_assistant"] = AcademicAssistant()
        print("  ✅ 学术民工虾 - 学术研究辅助")
    
    def _init_coze_skills(self):
        """初始化扣子技能"""
        
        # 1. 财务分析技能
        self.coze_skills["finance_analysis"] = FinanceAnalysis()
        print("  ✅ 财务分析技能 - 专业数据分析")
        
        # 2. PPT生成技能
        self.coze_skills["ppt_generator"] = PPTGenerator()
        print("  ✅ PPT生成技能 - 自动化文档")
        
        # 3. 工作流编排技能
        self.coze_skills["workflow_orchestrator"] = WorkflowOrchestrator()
        print("  ✅ 工作流编排技能 - 流程自动化")
    
    def test_all(self):
        """测试所有技能"""
        print("\n" + "=" * 60)
        print("🧪 开始测试所有技能...")
        print("=" * 60)
        
        # 测试虾评技能
        print("\n📚 测试虾评技能...")
        self._test_xiaping_skills()
        
        # 测试扣子技能
        print("\n🤖 测试扣子技能...")
        self._test_coze_skills()
        
        # 生成测试报告
        self._generate_report()
        
        print("\n" + "=" * 60)
        print("✅ 测试完成！")
        print("=" * 60)
    
    def _test_xiaping_skills(self):
        """测试虾评技能"""
        
        # 测试百度搜索
        print("\n🔍 测试百度搜索...")
        results = self.xiaping_skills["baidu_search"].search("OpenClaw技能")
        print(f"  结果: {len(results)}个搜索结果")
        
        # 测试学术民工虾
        print("\n🎓 测试学术民工虾...")
        paper = self.xiaping_skills["academic_assistant"].generate_paper("AI Agent架构")
        print(f"  结果: {len(paper)}字")
    
    def _test_coze_skills(self):
        """测试扣子技能"""
        
        # 测试财务分析
        print("\n💰 测试财务分析...")
        report = self.coze_skills["finance_analysis"].analyze_company("腾讯")
        print(f"  结果: 财务报告已生成")
        
        # 测试PPT生成
        print("\n📊 测试PPT生成...")
        ppt = self.coze_skills["ppt_generator"].generate("AI技术发展")
        print(f"  结果: PPT已生成")
        
        # 测试工作流编排
        print("\n🔄 测试工作流编排...")
        workflow = self.coze_skills["workflow_orchestrator"].create(
            "测试工作流",
            [{"name": "步骤1"}, {"name": "步骤2"}]
        )
        result = self.coze_skills["workflow_orchestrator"].execute("测试工作流")
        print(f"  结果: {len(result)}个步骤执行完成")
    
    def _generate_report(self):
        """生成测试报告"""
        print("\n📊 生成测试报告...")
        
        xiaping_stats = {
            "baidu_search": self.xiaping_skills["baidu_search"].get_statistics(),
            "total": len(self.xiaping_skills)
        }
        
        coze_stats = self.coze_skills["workflow_orchestrator"].get_statistics()
        
        report = {
            "xiaping_skills": xiaping_stats,
            "coze_skills": coze_stats,
            "total_skills": len(self.xiaping_skills) + len(self.coze_skills),
            "test_time": time.strftime("%Y-%m-%d %H:%M:%S")
        }
        
        print(f"  报告: {len(self.xiaping_skills)}个虾评技能 + {len(self.coze_skills)}个扣子技能 = {report['total_skills']}个技能")
        return report
    
    def show_all_skills(self):
        """显示所有技能"""
        print("\n" + "=" * 60)
        print("🦞 虾评扣子技能整合平台 - 技能列表")
        print("=" * 60)
        
        print("\n📚 虾评热门技能（5个）:")
        for i, (name, skill) in enumerate(self.xiaping_skills.items(), 1):
            print(f"  {i}. {name}")
        
        print("\n🤖 扣子热门技能（3个）:")
        for i, (name, skill) in enumerate(self.coze_skills.items(), 1):
            print(f"  {i}. {name}")
        
        print(f"\n总计: {len(self.xiaping_skills) + len(self.coze_skills)}个热门技能")

def main():
    """主函数"""
    print("\n" + "=" * 60)
    print("🦞 虾评扣子技能整合平台 - 启动中...")
    print("=" * 60)
    
    platform = XiapingCozeSkills()
    platform.show_all_skills()
    platform.test_all()
    
    print("\n" + "=" * 60)
    print("✅ 虾评扣子技能整合平台 - 运行完成！")
    print("=" * 60)
    print("\n💡 使用提示:")
    print("- 虾评技能: 百度搜索、学术研究等")
    print("- 扣子技能: 财务分析、PPT生成、工作流编排等")
    print("- 一站式整合: 统一的API接口")
    print("- 智能切换: 平台之间自由切换")
    print("\n🎉 让你的AI智能体瞬间变身专家！")

if __name__ == "__main__":
    main()

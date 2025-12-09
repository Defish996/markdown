#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
WorldQuant BRAIN平台操作符API获取脚本
直接调用BRAIN平台API获取最新的操作符信息
"""

import requests
import json
import getpass
import sys
from typing import Dict, List, Optional

class BrainAPI:
    """BRAIN平台API客户端"""
    
    def __init__(self):
        self.base_url = "https://api.worldquantbrain.com"
        self.session = requests.Session()
        self.token = None
        
    def login(self, email: str, password: str) -> bool:
        """登录BRAIN平台"""
        login_url = f"{self.base_url}/authentication"
        
        try:
            response = self.session.post(
                login_url,
                auth=(email, password)
            )
            
            if response.status_code == 201:
                print("✅ 登录成功!")
                self.token = response.headers.get('Authorization')
                if self.token:
                    self.session.headers.update({'Authorization': self.token})
                return True
            else:
                print(f"❌ 登录失败: {response.status_code} - {response.text}")
                return False
                
        except Exception as e:
            print(f"❌ 登录请求失败: {e}")
            return False
    
    def get_operators(self) -> Optional[Dict]:
        """获取操作符列表"""
        operators_url = f"{self.base_url}/operators"
        
        try:
            response = self.session.get(operators_url)
            
            if response.status_code == 200:
                return response.json()
            else:
                print(f"❌ 获取操作符失败: {response.status_code} - {response.text}")
                return None
                
        except Exception as e:
            print(f"❌ 获取操作符请求失败: {e}")
            return None
    
    def get_documentation(self) -> Optional[Dict]:
        """获取文档信息（可选）"""
        docs_url = f"{self.base_url}/documentations"
        
        try:
            response = self.session.get(docs_url)
            
            if response.status_code == 200:
                return response.json()
            else:
                # 文档端点可能不存在，这是正常的
                return None
                
        except Exception as e:
            # 文档获取失败不影响主要功能
            return None

def 格式化操作符信息(operators_data: Dict) -> str:
    """格式化操作符信息为可读格式"""
    if not operators_data or "operators" not in operators_data:
        return "未找到操作符数据"
    
    operators = operators_data["operators"]
    count = operators_data.get("count", len(operators))
    
    output = []
    output.append("=" * 80)
    output.append("WorldQuant BRAIN平台操作符列表")
    output.append("=" * 80)
    output.append(f"总计: {count} 个操作符\n")
    
    # 按类别分组
    categories = {}
    for op in operators:
        category = op.get("category", "未分类")
        if category not in categories:
            categories[category] = []
        categories[category].append(op)
    
    # 按类别输出
    for category, ops in categories.items():
        output.append(f"\n{'='*50}")
        output.append(f"类别: {category}")
        output.append(f"{'='*50}")
        
        for i, op in enumerate(ops, 1):
            output.append(f"\n{i}. 操作符名称: {op.get('name', 'N/A')}")
            output.append(f"   定义: {op.get('definition', 'N/A')}")
            output.append(f"   描述: {op.get('description', 'N/A')}")
            output.append(f"   使用范围: {', '.join(op.get('scope', []))}")
            output.append(f"   级别: {op.get('level', 'N/A')}")
            if op.get('documentation'):
                output.append(f"   文档: {op.get('documentation')}")
    
    return "\n".join(output)

def 保存操作符数据(operators_data: Dict, filename: str = "brain_operators.json"):
    """保存操作符数据到JSON文件"""
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(operators_data, f, ensure_ascii=False, indent=2)
        print(f"✅ 操作符数据已保存到 {filename}")
        return True
    except Exception as e:
        print(f"❌ 保存文件失败: {e}")
        return False

def 生成快速参考表(operators_data: Dict) -> str:
    """生成操作符快速参考表"""
    if not operators_data or "operators" not in operators_data:
        return "未找到操作符数据"
    
    operators = operators_data["operators"]
    
    output = []
    output.append(f"\n{'='*80}")
    output.append("操作符快速参考表")
    output.append(f"{'='*80}")
    
    categories = {}
    for op in operators:
        category = op.get("category", "未分类")
        if category not in categories:
            categories[category] = []
        categories[category].append(op)
    
    for category, ops in categories.items():
        output.append(f"\n{category}:")
        for op in ops:
            name = op.get('name', 'N/A')
            definition = op.get('definition', 'N/A')
            # 简化定义显示
            if len(definition) > 50:
                definition = definition[:47] + "..."
            output.append(f"  {name}: {definition}")
    
    return "\n".join(output)


# ========================= 仅新增 / 修改的部分 =========================
# ========================= 仅新增 / 修改的部分 =========================
OUTPUT_MODE = 'csv'          # 开关：'json' | 'csv' | 'terminal'

def 标准化操作符列表(raw) -> List[Dict]:
    """
    把接口返回的各种形态统一成 List[Dict]
    1. 如果是 dict 且包含 "operators" 字段，取它
    2. 如果是 list，直接返回
    3. 其它情况返回空列表
    """
    if isinstance(raw, dict) and "operators" in raw:
        return raw["operators"]
    if isinstance(raw, list):
        return raw
    return []

def 保存为JSON(operators_data: List[Dict], filename: str = "brain_operators.json"):
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(operators_data, f, ensure_ascii=False, indent=2)
        print(f"✅ 操作符数据已保存到 {filename}")
        return True
    except Exception as e:
        print(f"❌ 保存 JSON 失败: {e}")
        return False

def 保存为CSV(operators_data: List[Dict], filename: str = "brain_operators.csv"):
    import csv, os
    try:
        rows = []
        for op in operators_data:
            rows.append([
                op.get("name", ""),
                op.get("category", ""),
                op.get("definition", ""),
                op.get("description", ""),
                ",".join(op.get("scope", [])),
                op.get("level", "")
            ])
        with open(filename, 'w', newline='', encoding='utf-8-sig') as f:
            w = csv.writer(f)
            w.writerow(["name", "category", "definition", "description", "scope", "level"])
            w.writerows(rows)
        print(f"✅ 操作符数据已保存到 {filename}")
        return True
    except Exception as e:
        print(f"❌ 保存 CSV 失败: {e}")
        return False


def main():
    """主函数"""
    print("🚀 BRAIN平台操作符API获取工具")
    print("=" * 50)
    
    # 获取用户凭证
    print("请输入BRAIN平台邮箱: ")
    email = "3133866171@qq.com"
    print("请输入BRAIN平台密码: ")
    password = "wyq20021113."
    
    if not email or not password:
        print("❌ 邮箱和密码不能为空")
        return
    
    # 创建API客户端
    api = BrainAPI()
    
    # 登录
    print("\n正在登录BRAIN平台...")
    if not api.login(email, password):
        return
    
    # 获取操作符
    print("\n正在获取操作符信息...")
    operators_data = api.get_operators()
    
    if not operators_data:
        print("❌ 无法获取操作符信息")
        return
    
    # 显示操作符信息
    formatted_output = 格式化操作符信息(operators_data)
    print(formatted_output)
    
    # 生成快速参考表
    quick_ref = 生成快速参考表(operators_data)
    print(quick_ref)
    
    # 把原始返回统一成 List[Dict]
    operators_list = 标准化操作符列表(operators_data)

    # 保存数据
    if OUTPUT_MODE == 'terminal':
        pass          # 前面已经 print 过
    elif OUTPUT_MODE == 'csv':
        保存为CSV(operators_list)
    else:  # json
        保存为JSON(operators_list)
    
    print("\n🎉 操作完成!")
    print("- 操作符数据已保存 ")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n❌ 用户中断操作")
    except Exception as e:
        print(f"\n❌ 程序执行出错: {e}")
        import traceback
        traceback.print_exc()
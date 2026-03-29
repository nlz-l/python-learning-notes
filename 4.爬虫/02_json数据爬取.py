"""
作业2：爬取JSON格式数据并提取关键信息
"""
import requests
import json

print("=" * 50)
print("任务2：爬取JSON数据")
print("=" * 50)

# 使用GitHub API获取JSON数据（无需认证）
url = "https://api.github.com/users/github"
response = requests.get(url)

# 保存JSON数据
json_data = response.json()
with open("爬虫/github_data.json", "w", encoding="utf-8") as f:
    json.dump(json_data, f, ensure_ascii=False, indent=2)

print("\nJSON数据已保存到: github_data.json")

# 提取关键信息
print("\n【提取的关键信息】:")
print(f"用户名: {json_data.get('login')}")
print(f"ID: {json_data.get('id')}")
print(f"类型: {json_data.get('type')}")
print(f"公开仓库数: {json_data.get('public_repos')}")
print(f"粉丝数: {json_data.get('followers')}")
print(f"关注数: {json_data.get('following')}")
print(f"创建时间: {json_data.get('created_at')}")
print(f"个人主页: {json_data.get('html_url')}")

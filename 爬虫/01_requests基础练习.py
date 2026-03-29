"""
作业1：使用Requests库连接网页，打印HTTP头并保存网页内容
"""
import requests

# 连接网页
url = "https://www.baidu.com"
response = requests.get(url)

print("=" * 50)
print("任务1：打印HTTP头和响应属性")
print("=" * 50)

# 打印HTTP头
print("\n【HTTP响应头】:")
for key, value in response.headers.items():
    print(f"{key}: {value}")

# 打印响应的各个属性
print("\n【响应属性】:")
print(f"状态码 (status_code): {response.status_code}")
print(f"编码 (encoding): {response.encoding}")
print(f"URL (url): {response.url}")
print(f"是否重定向 (is_redirect): {response.is_redirect}")
print(f"历史记录 (history): {response.history}")
print(f"请求耗时 (elapsed): {response.elapsed}")
print(f"Cookies: {response.cookies}")

# 保存网页内容
with open("爬虫/网页内容.html", "w", encoding="utf-8") as f:
    f.write(response.text)
print("\n网页内容已保存到: 网页内容.html")

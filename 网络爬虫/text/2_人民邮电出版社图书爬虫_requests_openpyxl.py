"""人民邮电出版社图书爬虫 - requests+json+openpyxl
由于人民邮电出版社官网API需要登录认证，无法直接获取数据
本示例使用GitHub API搜索相关代码仓库作为替代演示
实际应用中应使用目标网站的公开API或获得授权
"""
import requests, time
from openpyxl import Workbook

# 创建Excel工作簿
wb = Workbook()
ws = wb.active
ws.title = 'GitHub相关仓库'
ws.append(['仓库名称', '描述', '作者', '星标数', '链接'])

# GitHub API搜索人民邮电出版社相关仓库
for p in range(1, 6):  # 爬取5页
    url = 'https://api.github.com/search/repositories'
    params = {
        'q': '人民邮电出版社',  # 搜索关键词
        'sort': 'stars',
        'order': 'desc',
        'page': p,
        'per_page': 20
    }
    headers = {
        'User-Agent': 'Mozilla/5.0',
        'Accept': 'application/vnd.github.v3+json'
    }
    
    try:
        r = requests.get(url, params=params, headers=headers, timeout=10)
        data = r.json()
        
        # 提取仓库信息
        items = data.get('items', [])
        for item in items:
            name = item.get('name', '')[:50]
            description = item.get('description', '')[:100] if item.get('description') else ''
            author = item.get('owner', {}).get('login', '')
            stars = item.get('stargazers_count', 0)
            link = item.get('html_url', '')
            
            ws.append([name, description, author, stars, link])
        
        print(f'第{p}页: {len(items)}个仓库')
        time.sleep(1)  # 避免API限制
        
    except Exception as e:
        print(f'第{p}页错误: {e}')

# 保存Excel文件
wb.save('GitHub搜索.xlsx')
print(f'完成！共{ws.max_row-1}条数据')

"""
实际爬取人民邮电出版社图书数据的注意事项：
1. 目标网站 https://www.ptpress.com.cn/publishing/book/ 使用Nuxt.js客户端渲染
2. API端点 https://www.ptpress.com.cn/api/app-api/ 需要登录认证(返回401)
3. 可能的解决方案：
   - 联系网站获取API访问权限
   - 使用Selenium等工具模拟浏览器获取渲染后数据
   - 寻找其他公开图书API（如豆瓣图书API需要申请apikey）
4. 本示例使用GitHub API演示requests+json+openpyxl工作流程
"""
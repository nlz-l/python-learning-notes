import requests, time, re
from bs4 import BeautifulSoup
from openpyxl import Workbook

wb = Workbook()
ws = wb.active
ws.title = 'GitHub热门开源仓库'
ws.append(['项目名称', '作者', '项目描述', '编程语言', '总星标数',
           '本周新增星标', '许可证', '主题标签', '项目链接'])

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
}
BASE = 'https://github.com'
# 8个不同编程语言对应8页
LANGS = ['python', 'javascript', 'java', 'go', 'rust', 'typescript', 'c', 'c++']

for idx, lang in enumerate(LANGS, 1):
    print(f'========== 第{idx}页: {lang} ==========')
    # ==================== 步骤1: 获取数据 - 请求列表页HTML ====================
    url = f'{BASE}/trending/{lang}?since=weekly'
    resp = requests.get(url, headers=HEADERS, timeout=15)
    if resp.status_code != 200:
        print(f'请求失败(状态码:{resp.status_code})，跳过\n')
        continue
    # ==================== 步骤2: 解析数据 - BeautifulSoup解析HTML ====================
    soup = BeautifulSoup(resp.text, 'html.parser')
    repo_list = soup.select('article.Box-row')[:10]  # 每页取前10个仓库
    print(f'获取到 {len(repo_list)} 个仓库')

    for i, repo in enumerate(repo_list):
        try:
            # ==================== 步骤3: 提取数据 - CSS选择器+正则提取 ====================
            # --- 列表页字段 ---
            a_tag = repo.select_one('h2 a')
            href = a_tag['href'].strip().strip('/')
            author, name = href.split('/')[:2]

            desc_p = repo.select_one('p')
            description = desc_p.get_text(strip=True)[:200] if desc_p else ''

            lang_el = repo.select_one('[itemprop="programmingLanguage"]')
            language = lang_el.get_text(strip=True) if lang_el else ''
            # 提取总星标数
            total_stars = ''
            for link in repo.select('a'):
                if '/stargazers' in link.get('href', ''):
                    total_stars = link.get_text(strip=True)
                    break
            # 正则提取本周新增星标
            repo_text = repo.get_text()
            star_match = re.search(r'([\d,]+)\s*stars?\s*(today|this\s*week)', repo_text)
            stars_week = star_match.group(1) if star_match else ''
            # --- 详情页数据获取 ---
            detail_url = BASE + '/' + href
            # ==================== 步骤1: 获取详情页HTML ====================
            dr = requests.get(detail_url, headers=HEADERS, timeout=15)

            # ==================== 步骤2: 解析详情页 ====================
            dsoup = BeautifulSoup(dr.text, 'html.parser')

            # ==================== 步骤3: 提取详情页字段 ====================
            # 提取许可证（从About侧边栏查找）
            license_text = ''
            about = dsoup.select_one('.BorderGrid')
            if about:
                about_txt = about.get_text()
                lic_m = re.search(r'(\S+)\s*(license|License|LICENSE)', about_txt)
                if lic_m:
                    license_text = f'{lic_m.group(1)} {lic_m.group(2)}'

            # 提取主题标签
            topics = [t.get_text(strip=True) for t in dsoup.select('a.topic-tag')]

            # 写入Excel
            ws.append([name, author, description, language, total_stars,
                       stars_week, license_text, ', '.join(topics[:8]), detail_url])
            print(f'  [{i+1:2d}] {author}/{name}  [OK]')

            time.sleep(1)  # 控制请求频率，避免被限流

        except Exception as e:
            print(f'  [{i+1:2d}] 出错: {e}')
            continue

    print(f'第{idx}页完成\n')
    time.sleep(2)  # 每页间暂停
# ==================== 步骤4: 存储数据 - 保存为Excel文件 ====================
output_path = 'github_trending_data.xlsx'
wb.save(output_path)
print(f'\n爬取完成！共 {ws.max_row-1} 条数据，已保存至 {output_path}')

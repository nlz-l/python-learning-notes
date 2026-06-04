# 实验四作业 - 网页爬虫

## 爬取网页
1. **新浪新闻**：`https://news.sina.com.cn/china/`
2. **人民邮电出版社**：`https://www.ptpress.com.cn/publishing/book/`
3. **豆瓣电影Top250**：`https://movie.douban.com/top250`

## 爬取字段（≥5个）
| 网页 | 字段 |
|------|------|
| 新浪新闻 | 标题、简介、时间、详情、链接 |
| 人民邮电出版社 | 书名、作者、出版社、定价、链接 |
| 豆瓣电影 | 电影名称、评分、评价人数、简介、链接 |

## 文件说明

| 文件 | 行数 | 说明 |
|------|------|------|
| `1_新浪新闻爬虫_requests_openpyxl.py` | 17行 | 新浪新闻（API接口获取JSON数据） |
| `2_人民邮电出版社图书爬虫_requests_openpyxl.py` | 30行 | 图书数据（中国图书网） |
| `3_豆瓣电影爬虫_requests_openpyxl.py` | 40行 | 豆瓣Top250 |

## 运行方法
```bash
pip install requests openpyxl beautifulsoup4
python 1_新浪新闻爬虫_requests_openpyxl.py
python 2_人民邮电出版社图书爬虫_requests_openpyxl.py
python 3_豆瓣电影爬虫_requests_openpyxl.py
```

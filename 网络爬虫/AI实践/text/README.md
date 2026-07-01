# 网页爬虫实验四

本目录保存网页爬虫实验四的代码和说明，目标是从多个网站采集结构化数据，并将结果写入 Excel 文件。实验主要练习 requests 请求、JSON 数据解析、HTML 页面解析和 openpyxl 表格写入。

## 爬取目标

| 网站 | 地址 | 采集字段 |
| --- | --- | --- |
| 新浪新闻 | `https://news.sina.com.cn/china/` | 标题、简介、时间、详情、链接 |
| 人民邮电出版社图书 | `https://www.ptpress.com.cn/publishing/book/` | 书名、作者、出版社、定价、链接 |
| 豆瓣电影 Top250 | `https://movie.douban.com/top250` | 电影名称、评分、评价人数、简介、链接 |

## 文件说明

| 文件 | 说明 |
| --- | --- |
| `1_新浪新闻爬虫_requests_openpyxl.py` | 通过接口或页面数据采集新浪新闻，并保存到 Excel |
| `2_人民邮电出版社图书爬虫_requests_openpyxl.py` | 采集人民邮电出版社图书数据 |
| `3_豆瓣电影爬虫_requests_openpyxl.py` | 采集豆瓣电影 Top250 数据 |

## 环境依赖

```bash
pip install requests openpyxl beautifulsoup4
```

## 运行方式

```bash
python 1_新浪新闻爬虫_requests_openpyxl.py
python 2_人民邮电出版社图书爬虫_requests_openpyxl.py
python 3_豆瓣电影爬虫_requests_openpyxl.py
```

运行后会根据脚本逻辑生成对应的 Excel 结果文件。

## 注意事项

- 目标网站页面结构可能会变化，若字段提取失败，需要重新检查选择器或接口返回格式。
- 豆瓣等网站可能存在反爬限制，学习时应降低请求频率，并遵守网站规则。
- 如果中文文件名在命令行中无法正常输入，可以在编辑器中直接运行脚本。

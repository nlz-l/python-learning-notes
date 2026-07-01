# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
# useful for handling different item types with a single interface
import openpyxl
import pymysql
from itemadapter import ItemAdapter


class ExcelPipeline:

    def __init__(self): # 初始化
        self.wb = openpyxl.Workbook() # 创建一个工作簿
        self.ws = self.wb.active # 创建一个工作表
        self.ws.title = 'Top250' # 设置工作表名称
        self.ws.append(['标题', '评分', '主题','时长','简介']) # 添加表头

    def open_spider(self, spider): # 爬虫开始时执行
        pass

    def close_spider(self, spider): # 爬虫结束时执行
        self.wb.save('top250.xlsx')

    def process_item(self, item, spider): # 专用处理数据

        self.ws.append((item['title'], item['rank'], item['subject'], item['duration'], item['intro']))
        return item

class DbPipeline:
    def __init__(self):
        self.conn = pymysql.connect(host='localhost',port=3306, user='root', password='123456', db='spider', charset='utf8mb4')
        self.cursor = self.conn.cursor()
        self.data = []
    def close_spider(self, spider):
        if len(self.data) > 0:
            self._write_to_db()
        self.conn.close()

    def process_item(self, item, spider):
        self.data.append((item['title'], item['rank'], item['subject'], item['duration'], item['intro']))
        if len(self.data) == 100:
            self._write_to_db()
            self.data.clear()
        return item

    def _write_to_db(self):
        self.cursor.executemany(
            "insert into tb_top_movie(title, rating, subject, duration, intro) values(%s, %s, %s, %s, %s)",
            self.data
        )
        self.conn.commit()
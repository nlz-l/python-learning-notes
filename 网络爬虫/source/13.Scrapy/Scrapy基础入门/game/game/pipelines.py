# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import openpyxl
# 管道默认是不生效的,需要在setting.py中配置 ITEM_PIPELINES
class GamePipeline:

    def __init__(self): # 初始化
        self.wb = openpyxl.Workbook() # 创建一个工作簿
        self.ws = self.wb.active # 创建一个工作表
        self.ws.title = '游戏列表' # 设置工作表名称
        self.ws.append(['游戏名','游戏分类','发行时间']) # 添加表头

    def close_spider(self, spider): # 爬虫结束时执行
        self.wb.save('游戏列表.xlsx')

    def process_item(self, item, spider): # 专用处理数据的方法
        self.ws.append((item['name'], item['category'], item['date']))
        return item


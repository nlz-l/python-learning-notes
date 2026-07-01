import scrapy
from game.items import GameItem

class XiaoSpider(scrapy.Spider):
    name = "xiao" #爬虫名
    allowed_domains = ["4399.com"]  # 允许的域名
    start_urls = ["https://www.4399.com/flash/"] # 起始url

    def parse(self, response): # 解析函数
        # 分块提取
        li_list = response.xpath('//ul[@class="n-game cf"]/li')
        for li in li_list:
            game_item = GameItem()
            game_item['name'] = li.xpath('./a/b/text()').extract_first() #提取一项内容,没有也不报错,返回None
            game_item['category'] = li.xpath('./em/a/text()').extract_first()
            game_item['date'] = li.xpath('./em/text()').extract_first()

            yield game_item
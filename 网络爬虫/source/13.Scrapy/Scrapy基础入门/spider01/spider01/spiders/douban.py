
import scrapy
from scrapy import Request
from spider01.items import MovieItem


class DoubanSpider(scrapy.Spider):
    name = "douban"
    allowed_domains = ["movie.douban.com"]

    async def start(self):
        for page in range(10):
            yield Request(f'https://movie.douban.com/top250?start={page*25}&filter=')

    def parse(self, response):
        list_items = response.xpath('//*[@id="content"]/div/div[1]/ol/li')
        for list_item in list_items:
            detail_url = list_item.xpath('./div/div[2]/div[1]/a/@href').extract_first()
            # print(detail_url)
            movie_item = MovieItem()
            movie_item['title'] = list_item.xpath('./div/div[2]/div[1]/a/span[1]/text()').extract_first()
            movie_item['rank']= list_item.xpath('./div/div[2]/div[2]/div/span[2]/text()').extract_first()
            movie_item['subject'] = list_item.xpath('./div/div[2]/div[2]/p[2]/span/text()').extract_first()
            yield Request(url=detail_url,
                          callback=self.parse_detail,
                          cb_kwargs={'item':movie_item})
    def parse_detail(self,response,**kwargs):
        movie_item = kwargs['item']
        movie_item['duration'] = response.xpath('//*[@property="v:runtime"]/@content').extract()[0]
        movie_item['intro'] = response.xpath('//*[@property="v:summary"]/text()').extract_first()
        yield movie_item



        # hrefs_list = response.xpath('//*[@id="content"]/div/div[1]/div[2]/a/@href')
        #
        # for href in hrefs_list[1:]:
        #     url = f"https://movie.douban.com/top250"+f"{href}"
        #     yield Request(url)

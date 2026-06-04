import csv
import io

import scrapy

from my_scrapy.items import StudentInternetUsageItem


class Test2ScrapySpider(scrapy.Spider):
    name = "test2_scrapy"
    allowed_domains = ["raw.githubusercontent.com"]
    start_urls = [
        "https://raw.githubusercontent.com/pk673/Social-Media-Addiction-Analysis/main/ClassSurvey.csv"
    ]

    def __init__(self, limit="100", *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.limit = int(limit)

    def parse(self, response):
        text = response.text.lstrip("\ufeff")
        reader = csv.DictReader(io.StringIO(text))

        for index, row in enumerate(reader):
            if index >= self.limit:
                break

            item = StudentInternetUsageItem()
            item["student"] = row.get("Student")
            item["week"] = row.get("Week")
            item["whatsapp"] = row.get("Whatsapp")
            item["instagram"] = row.get("Instagram")
            item["snapchat"] = row.get("Snapchat")
            item["telegram"] = row.get("Telegram")
            item["facebook"] = row.get("Facebook")
            item["bereal"] = row.get("BeReal")
            item["tiktok"] = row.get("TikTok")
            item["wechat"] = row.get("WeChat")
            item["twitter"] = row.get("Twitter")
            item["linkedin"] = row.get("Linkedin")
            item["messages"] = row.get("Messages")
            item["total_screen_time"] = row.get("TotalSocialMediaScreenTime")
            item["hourly_open_count"] = row.get("Number of times opened (hourly intervals)")
            item["addiction_status"] = row.get("SocialMediaAddiction")
            yield item

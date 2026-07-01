# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class PodcastItem(scrapy.Item):
    collection_id = scrapy.Field()
    podcast_name = scrapy.Field()
    author = scrapy.Field()
    country = scrapy.Field()
    genre = scrapy.Field()
    track_count = scrapy.Field()
    release_date = scrapy.Field()
    feed_url = scrapy.Field()
    detail_url = scrapy.Field()
    artwork_url = scrapy.Field()
    copyright = scrapy.Field()


class StudentInternetUsageItem(scrapy.Item):
    student = scrapy.Field()
    week = scrapy.Field()
    whatsapp = scrapy.Field()
    instagram = scrapy.Field()
    snapchat = scrapy.Field()
    telegram = scrapy.Field()
    facebook = scrapy.Field()
    bereal = scrapy.Field()
    tiktok = scrapy.Field()
    wechat = scrapy.Field()
    twitter = scrapy.Field()
    linkedin = scrapy.Field()
    messages = scrapy.Field()
    total_screen_time = scrapy.Field()
    hourly_open_count = scrapy.Field()
addiction_status = scrapy.Field()

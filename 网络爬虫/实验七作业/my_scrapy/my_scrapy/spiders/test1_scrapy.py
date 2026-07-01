import json
from urllib.parse import urlencode

import scrapy
from my_scrapy.items import PodcastItem


class Test1ScrapySpider(scrapy.Spider):
    name = "test1_scrapy"
    allowed_domains = ["itunes.apple.com"]

    def __init__(self, keyword="technology", limit="100", *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.keyword = keyword
        self.limit = int(limit)

    def build_url(self):
        params = {
            "term": self.keyword,
            "media": "podcast",
            "entity": "podcast",
            "limit": self.limit,
            "country": "US",
        }
        return "https://itunes.apple.com/search?" + urlencode(params)

    async def start(self):
        url = self.build_url()
        yield scrapy.Request(url, callback=self.parse)



    def parse(self, response):
        data = json.loads(response.text)

        for podcast in data.get("results", []):
            item = PodcastItem()
            item["collection_id"] = podcast.get("collectionId")
            item["podcast_name"] = podcast.get("collectionName")
            item["author"] = podcast.get("artistName")
            item["country"] = podcast.get("country")
            item["genre"] = podcast.get("primaryGenreName")
            item["track_count"] = podcast.get("trackCount")
            item["release_date"] = podcast.get("releaseDate")
            item["feed_url"] = podcast.get("feedUrl")
            item["detail_url"] = podcast.get("collectionViewUrl")
            item["artwork_url"] = podcast.get("artworkUrl600") or podcast.get("artworkUrl100")
            item["copyright"] = podcast.get("copyright")
            yield item

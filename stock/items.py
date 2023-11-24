# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class stockItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class market_watch(scrapy.Item):
    url = scrapy.Field()
    Ticker = scrapy.Field()
    Name = scrapy.Field()
    Yield = scrapy.Field()
    CHG = scrapy.Field()


class market_watch_two(scrapy.Item):
    url = scrapy.Field()
    Ticker = scrapy.Field()
    Name = scrapy.Field()
    Last = scrapy.Field()
    CHG = scrapy.Field()
    CHG_perc = scrapy.Field()


class CryptoItem(scrapy.Item):
    # define the fields for your item here like:
    Name = scrapy.Field()
    Abbrivation = scrapy.Field()
    Price = scrapy.Field()
    Percent = scrapy.Field()

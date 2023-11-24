import scrapy
from stock.items import CryptoItem


class CionscryptoSpider(scrapy.Spider):
    name = "cionscrypto"
    allowed_domains = ["www.coindesk.com"]
    start_urls = ["https://www.coindesk.com/data/"]

    custom_settings = {"FEEDS": {
        "data/cions_crypto.csv": {"format": "csv"},
        "data/cions_crypto.json": {"format": "json"}
    }}

    def parse(self, response):
        a_tags = response.css('a.hYRdsb')
        for a_tag in a_tags:
            crypto_item = CryptoItem()
            crypto_item["Name"] = a_tag.css("h2::text").get(),
            crypto_item["Abbrivation"] = a_tag.css("h2 span::text").get(),
            crypto_item["Price"] = a_tag.css("div.right span::text").get(),
            crypto_item["Percent"] = a_tag.css("div.right div.percentage::text").get()

            yield crypto_item

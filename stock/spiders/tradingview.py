# import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class TradingviewSpider(CrawlSpider):
    name = "tradingview"
    allowed_domains = ["www.tradingview.com"]
    start_urls = ["https://www.tradingview.com/"]

    rules = (
        Rule(LinkExtractor(allow='markets/indices/quotes-all/'), callback="parse_item"),
        Rule(LinkExtractor(allow='markets/indices/quotes-major/'), callback="parse_item"),
        Rule(LinkExtractor(allow='markets/indices/quotes-us/'), callback="parse_item"),
        Rule(LinkExtractor(allow='markets/indices/quotes-snp/'), callback="parse_item"),
        Rule(LinkExtractor(allow='markets/indices/quotes-currency/'), callback="parse_item"),
    )

    custom_settings = {"FEEDS": {
        "data/trading.csv": {"format": "csv"},
        "data/trading.json": {"format": "json"}
    }}

    def parse_item(self, response):
        table_rows = response.css("tbody tr")
        for table_row in table_rows:
            abbr = table_row.css("td.onscroll-shadow a::text").get()
            name = table_row.css("td.onscroll-shadow sup::text").get()
            price = table_row.css("td:nth-child(2)::text").get()
            change_per_1D = table_row.css("td:nth-child(3) span::text").get()
            change_1D = table_row.css("td:nth-child(4) span::text").get()
            high_1D = table_row.css("td:nth-child(5)::text").get()
            low_1D = table_row.css("td:nth-child(6)::text").get()
            tech_r_1D = table_row.css("td:nth-child(7) div::text").get()
            yield {
                "url": response.url,
                "Name": name,
                "Abbrivation": abbr,
                "Price": price,
                "Change % 1D": change_per_1D,
                "Change 1D": change_1D,
                "High 1D": high_1D,
                "Low 1D": low_1D,
                "Technical Rating 1D": tech_r_1D,
            }

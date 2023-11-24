import scrapy
from stock.items import market_watch
from stock.items import market_watch_two


class MarketwatchSpider(scrapy.Spider):
    name = "marketwatch"
    allowed_domains = ["www.marketwatch.com"]
    start_urls = ["https://www.marketwatch.com/investing"]

    custom_settings = {"FEEDS": {
        "data/market_watch.csv": {"format": "csv"},
        "data/market_watch.json": {"format": "json"}
    }}

    def parse(self, response):
        bonds = response.css("div.list ul li:nth-child(7) a::attr(href)").get()
        futures = response.css("div.list ul li:nth-child(8) a::attr(href)").get()
        crypto = response.css("div.list ul li:nth-child(9) a::attr(href)").get()
        currency = f'https://www.marketwatch.com{response.css("div.list ul li:nth-child(10) a::attr(href)").get()}'
        yield scrapy.Request(bonds, callback=self.parser_bonds)
        yield scrapy.Request(futures, callback=self.parser_stocks)
        yield scrapy.Request(crypto, callback=self.parser_stocks)
        yield scrapy.Request(currency, callback=self.parser_stocks)

    def parser_bonds(self, response):
        table_row = response.css("tbody tr")
        for table_rows in table_row:
            ticker = table_rows.css("td.align--left a::text").get()
            name = table_rows.css("td.w55 a::text").get()
            gains = table_rows.css("td:nth-child(4) bg-quote::text").get()
            chg = table_row.css("td:nth-child(5) bg-quote::text").get()
            market = market_watch()
            market["url"] = response.url,
            market["Ticker"] = ticker,
            market["Name"] = name,
            market["Yield"] = gains,
            market["CHG"] = chg,
            yield market

    def parser_stocks(self, response: object) -> object:
        table_row = response.css("tbody tr")
        for table_rows in table_row:
            ticker = table_rows.css("td.align--left a::text").get()
            name = table_rows.css("td.w55 a::text").get()
            last = table_rows.css("td:nth-child(4) bg-quote::text").get()
            chg = table_rows.css("td:nth-child(5) bg-quote::text").get()
            chg_percent = table_rows.css("td:nth-child(6) bg-quote::text").get()
            market_two = market_watch_two()
            market_two["url"] = response.url,
            market_two["Ticker"] = ticker,
            market_two["Name"] = name,
            market_two["Last"] = last,
            market_two["CHG"] = chg,
            market_two["CHG_perc"] = chg_percent
            yield market_two

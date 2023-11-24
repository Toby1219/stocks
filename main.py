from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from stock.spiders.cionscrypto import CionscryptoSpider
from stock.spiders.marketwatch import MarketwatchSpider
from stock.spiders.tradingview import TradingviewSpider
from stock.spiders.tradingview2 import TradingviewSpider2


def main():
    settings = get_project_settings()
    process = CrawlerProcess(settings)

    process.crawl(CionscryptoSpider)
    process.crawl(MarketwatchSpider)
    process.crawl(TradingviewSpider)
    process.crawl(TradingviewSpider2)

    process.start()


if __name__ == '__main__':
    main()

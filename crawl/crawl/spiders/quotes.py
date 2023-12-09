import scrapy
from ..items import CrawlItem

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["https://quotes.toscrape.com"]

    def parse(self, response):

        items = CrawlItem()

        all_div_quotes = response.xpath('//div[@class="quote"]')

        for quotes in all_div_quotes:
            text = quotes.xpath('./span[@class="text"]/text()').extract()
            author = quotes.xpath('.//small[@class="author"]/text()').extract()
            tags = quotes.xpath('.//a[@class="tag"]/text()').extract()

            items['text'] = text
            items['author'] = author
            items['tags'] = tags

            yield items

        # ikisi de aynı sonucu verir
        #title = response.xpath('//div[@class="col-md-8"]/h1/a/text()').extract_first()
        # #title = response.xpath('//div[@class="col-md-8"]/h1/a/text()').get(







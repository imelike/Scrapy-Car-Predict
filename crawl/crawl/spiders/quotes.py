import scrapy
from scrapy.http import FormRequest
from scrapy.utils.response import open_in_browser
from ..items import CrawlItem

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = ["https://quotes.toscrape.com/login"]

    def parse(self, response):
        token = response.xpath('//form/input[@name="csrf_token"]/@value').extract_first()
        return FormRequest.from_response(response,formdata={
            'csrf_token': token,
            'username': 'imelike',
            'password': 'imelike'
        }, callback=self.start_scraping)

    def start_scraping(self, response):
        open_in_browser(response)
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







# # quotes.py nin yedeği
# # burada login olmadan site crawl edilir
#
# import scrapy
# from ..items import CrawlItem
#
# class QuotesSpider(scrapy.Spider):
#     name = "quotes"
#     page_number = 2
#     allowed_domains = ["quotes.toscrape.com"]
#     start_urls = ["https://quotes.toscrape.com/page/1/"]
#
#     def parse(self, response):
#
#         items = CrawlItem()
#
#         all_div_quotes = response.xpath('//div[@class="quote"]')
#
#         for quotes in all_div_quotes:
#             text = quotes.xpath('./span[@class="text"]/text()').extract()
#             author = quotes.xpath('.//small[@class="author"]/text()').extract()
#             tags = quotes.xpath('.//a[@class="tag"]/text()').extract()
#
#             items['text'] = text
#             items['author'] = author
#             items['tags'] = tags
#
#             yield items
#
#             next_page = "https://quotes.toscrape.com/page/" + str(QuotesSpider.page_number) + "/"
#             if QuotesSpider.page_number < 11:
#                 QuotesSpider.page_number += 1
#                 yield response.follow(next_page, callback=self.parse)
#
#
#
#         # ikisi de aynı sonucu verir
#         #title = response.xpath('//div[@class="col-md-8"]/h1/a/text()').extract_first()
#         # #title = response.xpath('//div[@class="col-md-8"]/h1/a/text()').get(
#
#
#
#
#
#

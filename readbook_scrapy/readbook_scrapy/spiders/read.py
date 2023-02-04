import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from readbook_scrapy.items import ReadbookScrapyItem

class ReadSpider(CrawlSpider):
    name = 'read'
    allowed_domains = ['www.dushu.com']
    start_urls = ['https://www.dushu.com/book/1188_1.html']

    rules = (
        Rule(LinkExtractor(allow=r'/book/1188_\d+\.html'), 
            callback='parse_item', 
            follow=True),
    )

    def parse_item(self, response):
       
        img_list = response.xpath('//div[@class="book-info"]//img')

        for img in img_list:

            src= img.xpath('./@data-original').extract_first()
            name = img.xpath('./@alt').extract_first()
            introdution=img.xpath('//p[@class="disc eps"]').extract_first()

            book = ReadbookScrapyItem(name=name ,src=src,introdution=introdution)

            yield book

       

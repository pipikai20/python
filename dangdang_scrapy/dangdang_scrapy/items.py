# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DangdangScrapyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    # 就是你要下载的数据有什么
    

    src = scrapy.Field()

    name = scrapy.Field()
    
    price = scrapy.Field()
    author = scrapy.Field()
    time = scrapy.Field()
    ditail = scrapy.Field()
    review = scrapy.Field()


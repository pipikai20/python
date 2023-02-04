# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DangdangwangItem(scrapy.Item):
    
    name = scrapy.Field()

    price = scrapy.Field()

    title = scrapy.Field()

    author = scrapy.Field()

    # 出版社
    press = scrapy.Field()

    # 评论
    comment = scrapy.Field()

    # 内容
    content = scrapy.Field()

    btime =scrapy.Field()


import scrapy


class TcSpider(scrapy.Spider):
    name = 'tc'
    allowed_domains = ['http://jm.58.com']
    start_urls = ['http://jm.58.com/']

    def parse(self, response):
        # print('学习')
        # 字符串
        # content =response.text


        # 二进制
        # content= response.body
        # print('=========================')
        # print(content)


        span=response.xpath('//div[@id="filter"]/div[@class="tabs"]/a/span')[0]
        print('=====================')
        print(span.extract())
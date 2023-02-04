import scrapy
from  move_scrapy.items import MoveScrapyItem

class MovieSpider(scrapy.Spider):
    name = 'movie'
    # 一般只写域名
    allowed_domains = ['www.ygdy8.net']
    start_urls = ['https://www.ygdy8.net/html/gndy/china/index.html']

    def parse(self, response):
        # 需要第一个的名字和第二页的图片
        a_list = response.xpath('//div[@class="co_content8"]//a[2]')

        for a in a_list:
            name = a.xpath('./text()').extract_first()
            href = a.xpath('./@href').extract_first()

            # 第二页的地址是
            url = 'https://www.ygdy8.net' + href
            # print(name,url)

            yield scrapy.Request(url=url,callback=self.parse_second,meta={'name':name})


    # 跳转页的图片地址
    def parse_second(self,response):
        # 如果拿不到数据 就要检查xpath语法
        src =response.xpath('//div[@id="Zoom"]//img/@src').extract_first()

        # 接收到请求的那个meta参数的值
        name = response.meta['name']

        movie = MoveScrapyItem(src=src,name=name)
        # print(src)

        yield movie



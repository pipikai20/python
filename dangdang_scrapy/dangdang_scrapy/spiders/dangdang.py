import scrapy
from dangdang_scrapy.items import DangdangScrapyItem
# DangdangScrapyItem

class DangdangSpider(scrapy.Spider):
    name = 'dangdang'
    # 如果是多页下载 必须调整 allowed_domains的范围 一般是删除http://和com以后的东西
    allowed_domains = ['category.dangdang.com']
    start_urls = ['http://bang.dangdang.com/books/bestsellers']

    def parse(self, response):
       
        li_list = response.xpath('//div[@class="bang_list_box"]/ul/li')

        for li in li_list:

            # src = li.xpath('.//img/@data-original').extract_first()
            # # 因为当当网除了第一张图片，其他都做了懒加载
            # # 第一张是scr  以后都是data-original

            # if src:
            #     src =src 
            
            # else:  
            #   src = li.xpath('.//img/@src').extract_first()


            name = li.xpath('.//div[@class="name"]/a/text()').extract_first()
            
            price = li.xpath('./div[@class="price"]/p/span[1]/text()').extract_first()
            author=li.xpath('.//div[@class="publisher_info"]/a/text()').extract_first()
            time=li.xpath('.//div[@class="publisher_info"]/span/text()').extract_first()
            ditail=li.xpath('.//div[@class="name"]/a/text()').extract_first()
            review=li.xpath('.//div[@class="star"]/a/text()').extract_first()

            print(str(name),review,author,time,price,ditail)

            book =DangdangScrapyItem(name=name,review=review,author=author,time=time,price=price,ditail=ditail)


            #获取一个book就将book交给pipeline 

            # 记得在setting文件中解开注释： ITEM_PIPELINES = {
           # 'dangdang_scrapy.pipelines.DangdangScrapyPipeline': 300,}

            # 在item中添加src = scrapy.Field()

            # pipeline中添加下载文件

            yield book


            # 每一页的爬取业务逻辑是一样的 ，所以多页下载的操作是只需要将执行的那页的请求再次调用parse方法

            # http://category.dangdang.com/pg2-cp01.25.01.00.00.00.html  第二页
            # http://category.dangdang.com/pg3-cp01.25.01.00.00.00.html  第三页
            # http://category.dangdang.com/pg4-cp01.25.01.00.00.00.html  第四页


        if self.page <100:
            self.page = self.page+1
            
            url = self.base_url + str(self.page) +'-cp01.25.01.00.00.00.html'


            # scrapy.Requset就是scrapy的get请求 url是请求地址，callback是你要执行的那个函数，不允许添加圆括号
            yield scrapy.Request(url=url,callback=self.parse)



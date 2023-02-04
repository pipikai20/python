import scrapy
from dangdangwang.items import DangdangwangItem
import time
import re

class DangdangSpider(scrapy.Spider):
    name = 'dangdang'
    allowed_domains = ['dangdang.com']
    start_urls = ['http://bang.dangdang.com/books/bestsellers']
    page_next_id = 2

    def parse(self, response):
        for dd in response.xpath('//div[@class="bang_list_box"]/ul/li'):

            time.sleep(5)
            item = DangdangwangItem()
        # 书名
            name = dd.xpath('./div[@class="name"]/a/text()').extract()
            if len(name) > 0:
                
                str=name[0]+"）"
                item['name'] = re.sub(u"\\（.*?）|\\{.*?}|\\[.*?]|\\【.*?】|\\.*?）", "",str.encode('utf-8').decode())
     
            else:
                item['name'] = ""
            
        # 价格
            price = dd.xpath('./div[@class="price"]/p/span[1]/text()').extract()
            if len(price) > 0:
                item['price'] = price[0].replace("¥", "")
            else:
                item['price'] = ""
            
        # 标题
            title = dd.xpath('.//div[@class="name"]/a/text()').extract()
            if len(title) > 0:
                item['title'] = title[0]
            else:
                item['title'] = ""
           
        # 作者
            author = dd.xpath('.//div[@class="publisher_info"]/a/text()').extract()
            if len(author) > 0:
                item['author'] = author[0]
            else:
                item['author'] = ""
        # 出版社
            press = dd.xpath('./div[@class="publisher_info"][2]/a[1]/text()').extract()
            if len(press) > 0:
                item['press'] = press[0]
            else:
                item['name'] = ""
            
        # 出版时间
            btime = dd.xpath('.//div[@class="publisher_info"]/span/text()').extract()
            if len(press) > 0:
                item['btime'] = btime[0]
            else:
                item['btime'] = ""
        # 评论数目
            comment = dd.xpath('.//div[@class="star"]/a/text()').extract()
            if len(comment) > 0:
                item['comment'] = comment[0].replace("条评论", "")
            else:
                item['comment'] = ""
            
        # 简介
            content = dd.xpath('.//div[@class="name"]/a/text()').extract()
            if len(content) > 0:
                item['content'] = content[0]
            else:
                item['content'] = ""
            
            yield item
        # 爬取多页数据
        page_next_url = "http://bang.dangdang.com/books/bestsellers/1-{}".format(
            self.page_next_id)
        # 排行榜共26页
        if self.page_next_id < 26:
            

            yield scrapy.Request(url=page_next_url, dont_filter=True, callback=self.parse)
            

            self.page_next_id += 1


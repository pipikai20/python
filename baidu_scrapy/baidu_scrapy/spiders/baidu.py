import scrapy


class BaiduSpider(scrapy.Spider):
    # 爬虫的名字  勇于爬虫的时候 使用的值
    name = 'baidu'
    # 允许访问的域名
    allowed_domains = ['http://www.baidu.com']


    # 起始url地址 指的是第一次要访问的域名
    # start_url 是在allowed_domains的前面加http://
                    # 在allowed_domains的后面添加一个/
    
    # 是执行了start_urls之后 执行的方法 方法中response就是返回的对象
    start_urls = ['http://www.baidu.com/']

    def parse(self, response):
        print('学习')

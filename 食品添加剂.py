from scrapy.selector import Selector
import urllib.request
import urllib.response
url='http://bang.dangdang.com/books/bestsellers'

headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'}

request=urllib.request.Request(url=url,headers=headers)

# 模拟浏览器向服务器发送请求
response= urllib.request.urlopen(request)

# 获取响应内容
content =response.read().decode('utf-8')


# from lxml import etree

li_list = response.xpath('//div[@class="bang_list_box"]/ul/li')

for li in li_list:

    name = li.xpath('.div[@class="name"]/a').extract_first()



# for dd in response.xpath("//div[@class='bang_list_box']/ul/li"):

#   name = dd.xpath(".div[@class='name']/a/text()").extract()
# # tree = etree.HTML(content)
# result = tree.xpath('//div[@class="name"]/text()')[0]



print(name )

# 数据下载本地
# # open方法默认情况下使用的是gbk的编码 如果要保存中文 需要在open方法中指定编码格式为utf-8
# fp=open('豆瓣.json','w',encoding='utf-8')
# fp.write(content)
# get 请求
# 获取豆瓣电影第一页数据 并保存

import urllib.request

url='https://juejin.cn/post/7129685508589879327'

headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'}

request=urllib.request.Request(url=url,headers=headers)

# 模拟浏览器向服务器发送请求
response= urllib.request.urlopen(request)

# 获取响应内容
content =response.read().decode('utf-8')

# print(content)

# # 数据下载本地
# # open方法默认情况下使用的是gbk的编码 如果要保存中文 需要在open方法中指定编码格式为utf-8
# fp=open('juejin.html','w',encoding='utf-8')
# fp.write(content)


# 解析网页源码 来获取我们想要的数据
from lxml import etree

# 解析服务器响应的文件
tree = etree.HTML(content)

# 获取想要的数据 xpath返回的值是一个列表类型的数据
result = tree.xpath ( '//article[@itemscope="itemscope"]/text()')[0]

print(result)

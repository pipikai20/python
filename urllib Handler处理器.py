# 需求使用handler来访问百度 获取页面源码

from cgitb import handler
from urllib import response
import urllib.request

url='http://baidu.com'

headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'}

request = urllib.request.Request(url=url,headers=headers)

# handler  bulid_open  open

# (1)获取handler对象
handler = urllib.request.HTTPHandler()

# (2)获取opener对象
opener =urllib.request.build_opener(handler)

# (3)调用open方法
response=opener.open(request)

content =response.read().decode('utf-8')

print(content)
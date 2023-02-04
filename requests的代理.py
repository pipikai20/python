from urllib import response
from weakref import proxy
import requests

url ='http://www.baidu.com/s'

headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'}

data ={
    'wd':'ip'
}
# 代理
proxy = {

    'http':'60.170.204.30:8060'
}

response =requests.get(url=url ,params=data,headers=headers,proxies=proxy)

content =response.text

with open('daili.html','w',encoding='utf-8')as fp:
    fp.write(content)
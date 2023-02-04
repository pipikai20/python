from http.client import HTTPS_PORT
from urllib import response
import urllib.request

url='https://www.baidu.com'


# url的组成
# http/https    www.baidu.com     80/443
# 协议           主机           端口号          路径      参数          据点
# http    80
# HTTPS   443
# mysql    33056
# oracle     1521
# redis      6379
# mongodb    27017

# ua 是进入网页后f12中的network 的header中最底下的ua
# 这是ua反爬
headers ={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'}


# 因为urlopen方法不能存储字典  所以headers不能传递进去
# 请求对象的定制

request = urllib.request.Request(url=url,headers=headers)

response = urllib.request.urlopen(request)

content = response.read().decode('utf-8')

print(content)
    
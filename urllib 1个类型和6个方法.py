from email import contentmanager
from urllib import response
import urllib.request

url = 'https://www.baidu.com'

# 模拟器浏览器向服务器请求
response = urllib.request.urlopen(url)

# 一个类型和六个方法
#  respones是HTTPResponse的类型
print(type(response))


# 按照一个字节一个字节的读
content =response.read()
print(content)
# 返回多少字节
content =response.read(5)
print(content)



# 读取一行
content =response.readline()
print(content)


# 读取多行
content = response.readlines()
print(content)


# 返回状态码 如果是200了 那么证明我们的逻辑没有问题
print(response.getcode())



# 返回的是url的地址
print(response.url())



# 获取是一个状态信息
print(response.getheaders())



# 一个类型HHTPRsponse

# 六个方法 read readline readlines getcode geturl getheaders


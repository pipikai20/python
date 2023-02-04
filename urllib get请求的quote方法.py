# https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=78000241_45_hao_pg&wd=%E7%8E%8B%E4%BF%8A%E5%87%AF

# 需求 获取 https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=78000241_45_hao_pg&wd=王俊凯的网页源码


from urllib import response
import urllib.request
from wsgiref import headers

url='https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=78000241_45_hao_pg&wd='


# 请求对象的定制为了解决反爬
headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'}
# 将王俊凯三个字变成unicod的编码格式
# 我们需要依赖于urllib.parse

name=urllib.parse.quote('王俊凯')


url= url+ name

print(url) 

# 请求对象定制
request = urllib.request.Request(url=url,headers=headers)

# 模拟浏览器向服务器发送请求
response= urllib.request.urlopen(request)

# 获取响应内容
content =response.read().decode('utf-8')

# 打印数据
print(content)
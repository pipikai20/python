# urlencode 应用场景：多个参数的时候

# https://www.baidu.com/s?wd=王俊凯&sex=男

from urllib import response
import urllib.parse

data={
    'wd':'王俊凯',
    'sex':'男'
}

a=urllib.parse.urlencode(data)
print(a)


# 获取http://baidu.com/s?wd=%E7%8E%8B%E4%BF%8A%E5%87%AF&sex=%E7%94%B7 网页源代码

import urllib.request
import urllib.parse


base_url='http://baidu.com/s?'

data={
    'wd':'王俊凯',
    'sex':'男',
    'location':'中国重庆'
    
}

new_data= urllib.parse.urlencode(data)

# 请求资源路径
url= base_url + new_data

headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'}


# 请求对象定制
request = urllib.request.Request(url=url,headers=headers)

# 模拟浏览器向服务器发送请求
response= urllib.request.urlopen(request)

# 获取响应内容
content =response.read().decode('utf-8')

# 打印数据
print(content)


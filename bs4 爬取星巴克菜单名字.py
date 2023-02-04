import urllib.request
 
url = 'https://www.starbucks.com.cn/menu/'

headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'}

request=urllib.request.Request(url=url,headers=headers)

# 模拟浏览器向服务器发送请求
response= urllib.request.urlopen(request)

# 获取响应内容
content =response.read().decode('utf-8')

print(content)


# //ul[@class="grid padded-3 product"]//strong/text()

from bs4 import BeautifulSoup

soup = BeautifulSoup(content,'lxml')

name_list = soup.select('ul[class="grid padded-3 product"] strong')

for name in name_list:
    print(name.string)


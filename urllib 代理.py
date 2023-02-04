from cgitb import handler
import urllib.request

url='https://www.baidu.com/s?wd=ip'

headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'}

request = urllib.request.Request(url=url,headers=headers)

# response = urllib.request.urlopen(request)

# 代理 快代理网站    'http':'ip:port'   不行多试几个
proxies={
    'http':'223.96.90.216:8085'
}

# handler build_open  open
handler=urllib.request.ProxyHandler(proxies =proxies)

opener = urllib.request.build_opener(handler)

response=opener.open(request)

content = response.read().decode('utf-8')

with open('代理.html','w',encoding='utf-8')as fp:
    fp.write(content)
    
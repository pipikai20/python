import urllib.request

proxies_pool=[
{'http':'223.96.90.216:8085'},
{'http':'223.96.90.216:8085'}

]

import random
proxies =random.choice(proxies_pool)

url='https://www.baidu.com/s?wd=ip'

headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'}

request = urllib.request.Request(url=url,headers=headers)

# handler build_open  open
handler=urllib.request.ProxyHandler(proxies =proxies)

opener = urllib.request.build_opener(handler)

response=opener.open(request)

content = response.read().decode('utf-8')

with open('代理2.html','w',encoding='utf-8')as fp:
    fp.write(content)
    
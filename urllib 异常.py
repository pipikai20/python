from email import header
import imp

import urllib.request
import urllib.error

# url='https://blog.csdn.net/weixin_37493499/article/details/125485736'

url='http://dfs fsfsf.com'

headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'}


try:
    request=urllib.request.Request(url=url,headers=headers)

# 模拟浏览器向服务器发送请求
    response= urllib.request.urlopen(request)

# 获取响应内容
    content =response.read().decode('utf-8')

    print(content)

except urllib.error.HTTPError:
    print('系统正在升级...')

except urllib.error.HTTPError:
    print('系统正在升级...')

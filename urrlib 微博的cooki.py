# 适用场景：数据采集的时候 需要绕过登录 然后进入到某人页面

import urllib.request

import urllib.response

url='https://weibo.com/u/6312434822'

headers={
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
    # ':authority':' weibo.com',
    # ':method'':'' GET',
    # ':path'':'' /ajax/profile/info?uid=6312434822',
    # ':scheme':' https',
    'accept':' application/json, text/plain, */*',
    # 'accept-encoding':' gzip, deflate, br',
    'accept-language':' zh-CN,zh;q=0.9',
    'client-version':' v2.36.2',
    'cookie':' PC_TOKEN=151af9d4de; XSRF-TOKEN=0oGjlCpmsYD2kEaMC9-oXezd; SUB=_2A25OR_PVDeRhGeBN6lAV8yrEyT6IHXVtNWIdrDV8PUNbmtANLVXgkW9NRJcUqgQ6U4gnNPTF1hoMVQ5hMe80pCHz; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFWgu7BuYb1AjgzpmucmKkH5JpX5KzhUgL.Foq0eKzXe0BReoz2dJLoIf2LxKBLBonL1h5LxKBLBonLB-2LxK-L1KqL1-eLxKqLB-eLBKzLxKML1hzLBo.LxKML1hzLBo.LxKML1-2L1hBLxK-LBK-LBoeLxK-LB-BLBK.t; ALF=1696904964; SSOLoginState=1665368965; WBPSESS=qCEiQp97_Q27YMnQ84V9hxfXsqD8YUsvBtzY0L3y52zkhyiWxXnSP2qITLnnSBlnzGBx_a4W7FIFThOE2pOt41fqNryFt7D5R2fkUjlhiGHuXynJ09-FxOOV0flbKnVVoI9t4IVnB_zPRm3qBhbZ9g==',
    'referer': 'https://weibo.com/u/6312434822',
    'sec-ch-ua':' "Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
    'sec-ch-ua-mobile':' ?0',
    'sec-ch-ua-platform':' "Windows"',
    'sec-fetch-dest':' empty',
    'sec-fetch-mode':' cors',
    'sec-fetch-site':' same-origin',
    'server-version':' v2022.10.09.1',
    'traceparent':' 00-87e7621d4ce7cbbd83818d22eca2f5b8-5b7358b29808637a-00',
    'user-agent':' Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
    'x-requested-with':' XMLHttpRequest',
    'x-xsrf-token':' 0oGjlCpmsYD2kEaMC9-oXezd',
    }


# 请求对象定制
request = urllib.request.Request(url=url,headers=headers)

# 模拟浏览器向服务器发送请求
response= urllib.request.urlopen(request)

# 获取响应内容
content =response.read().decode('utf-8')

# 将数据保存到本地
with open('weibo1.html','w',encoding='utf-8')as fp:
    fp.write(content)

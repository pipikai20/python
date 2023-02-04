# 通过登录 然后进入主页面



# 表单数据
# __VIEWSTATE: eN88S/ozxNGBLmN5/Ivubl6L6KQMO65F9gerwHgwh54oR/YTw9NceBA9+JPOq66ob84+bvqcTSyoi0B8wp6hskZXe8cBJY3fAMl6zDCKDw3bviZtwZcnnfBoG6F6fgA1pORUlrNfkn+RiVV+0HaFjU6tzh8=
# __VIEWSTATEGENERATOR: C93BE1AE
# from: http://so.gushiwen.cn/user/collect.aspx
# email:  18022028838
# pwd: 12326105650
# code: qes2
# denglu: 登录


#  __VIEWSTATE:   __VIEWSTATEGENERATOR:   code 是一个可以变化的量

# 难点：（1）__VIEWSTATE:   __VIEWSTATEGENERATOR:   一般情况下看不到的数据 再页面的源代码
        # 观察到这两个数据在页面源代码中 所以我们需要获取页面的源码 然后进行解析就可以获取的

        # （2）验证码


import requests
# 登录页面的url地址
url='https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx'

headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'}


response =requests.post(url=url , headers=headers)

content = response.text

# 解析页面源码 获取__VIEWSTATE:   __VIEWSTATEGENERATOR: 

from bs4 import BeautifulSoup

soup = BeautifulSoup(content,'lxml')

# 获取__VIEWSTATE

VIEWSTATE =soup.select('#__VIEWSTATE')[0].attrs.get('value')


# 获取__VIEWSTATEGENERATOR
VIEWSTATEGENERATOR = soup.select('#__VIEWSTATEGENERATOR')[0].attrs.get('value')


# 获取验证码图片
code = soup.select('#imgCode')[0].attrs.get('src')

code_url = 'https://so.gushiwen.cn' + code

# requests 里面有一个方法 session（） 通过session的返回值 就能使用请求变成一个对象

session =requests.session()

# 验证码的url的内容
response_code =session.get(code_url)

# 注意此时要使用二进制数据 因为我们要使用的是图片的下载
content_code = response_code.content

# wb的模式就是将二进制数据写入文件
with open('code.jpg','wb')as fp:
    fp.write(content_code)



# 获取了验证码的图片之后 下载到本地 观察验证码 在控制台输入这个验证码 就可以将这个值给 code的参数 就可以登录

code_name = input('请输入你的验证码')

# print(VIEWSTATE)
# print(VIEWSTATEGENERATO)

url_post ='https://so.gushiwen.cn/user/login.aspx?from=http%3a%2f%2fso.gushiwen.cn%2fuser%2fcollect.aspx'

data_post = {
    '__VIEWSTATE':VIEWSTATE,
    '__VIEWSTATEGENERATOR':VIEWSTATEGENERATOR,
    'from': 'http://so.gushiwen.cn/user/collect.aspx',
    'email': '18022028838',
    'pwd': '18022028838',
    'code': code_name,
    'denglu': '登录'
}

response_post = session.post(url=url,headers=headers,data=data_post)

contnet_post =response_post.text

with open ('gushiwen.html','w',encoding='utf-8')as fp:
    fp.write(contnet_post)

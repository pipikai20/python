from urllib import response
import requests

url = 'https://www.baidu.com/s'

headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'}

data ={
    'wd':'北京'
}


# url 请求资源路径
# parmas 参数
# kwargs 字典

response = requests.get(url =url,params=data,headers=headers)

content =response.text


print(content)
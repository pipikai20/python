from urllib import response
import requests

url = 'https://fanyi.baidu.com/v2transapi?from=en&to=zh'

headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'}

data = {
    'query': 'eye'
}

response =requests.post(url=url , data=data,headers=headers)

content = response.text


import json
obj = json.loads(content)
print(obj)
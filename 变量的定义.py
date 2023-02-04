import requests
import json

url = "https://api.juejin.cn/user_api/v1/author/recommend?aid=2608&uuid=7140909935034779176&spider=0&category_id=&cursor=0&limit=20"
info = {"id_type":2,"client_type":2608,"sort_type":200,"cursor":"0","limit":20}
headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36',
}
has_more = True
payload = '{"operationName":"","query":"","variables":{"ownerId":"5c3f3c415188252b7d0ea40c","size":20,"after":""},"extensions":{"query":{"id":"b158d18c7ce74f0d6d85e73f21e17df6"}}}'

# 发起网络请求，获取到返回的html
requests.adapters.DEFAULT_RETRIES = 5
result = requests.post(url=url, headers=headers, data=payload).content.decode('utf-8')
print(result)

# result=json.loads(result)
# result_list=result['data']['ownActivityFeed']['items']['edges']
# print(result_list)


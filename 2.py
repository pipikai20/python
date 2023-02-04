import imp
import urllib.request
from lxml import etree
url='https://api.juejin.cn/recommend_api/v1/article/recommend_all_feed?aid=2608&uuid=7140909935034779176&spider=0'

headers={
   'cookie': '_ga=GA1.2.230441076.1662622666; _tea_utm_cache_2608=undefined; __tea_cookie_tokens_2608=%257B%2522web_id%2522%253A%25227140909935034779176%2522%252C%2522user_unique_id%2522%253A%25227140909935034779176%2522%252C%2522timestamp%2522%253A1662622669100%257D; passport_csrf_token=384b0ce75f096593882986acec8ccd87; passport_csrf_token_default=384b0ce75f096593882986acec8ccd87; odin_tt=149c2ced2b165d7d5dd24360432c83d9d766e332def512fa411815c0817d9c36207c71137a4425d79df9385b64737fa611b79bfa015858c505d9babef85be8d0; sid_guard=97c7a34b7f26aa7caad4492b63ceb689%7C1663292009%7C31536000%7CSat%2C+16-Sep-2023+01%3A33%3A29+GMT; uid_tt=2471c16a091daeb6885a0085f94e35b1; uid_tt_ss=2471c16a091daeb6885a0085f94e35b1; sid_tt=97c7a34b7f26aa7caad4492b63ceb689; sessionid=97c7a34b7f26aa7caad4492b63ceb689; sessionid_ss=97c7a34b7f26aa7caad4492b63ceb689; sid_ucp_v1=1.0.0-KDhmNTBjM2M1MmQzYzcxMzQ5NDE5MWYzMWY0MGMxNjBjYjYzMTZlMjMKFgiN47Dpo4zTBRDppI-ZBhiwFDgIQAsaAmxmIiA5N2M3YTM0YjdmMjZhYTdjYWFkNDQ5MmI2M2NlYjY4OQ; ssid_ucp_v1=1.0.0-KDhmNTBjM2M1MmQzYzcxMzQ5NDE5MWYzMWY0MGMxNjBjYjYzMTZlMjMKFgiN47Dpo4zTBRDppI-ZBhiwFDgIQAsaAmxmIiA5N2M3YTM0YjdmMjZhYTdjYWFkNDQ5MmI2M2NlYjY4OQ; n_mh=0h95KTRww6yUY_mjtS7zXgBsCrYPR9efQydN5iuiglk; MONITOR_WEB_ID=c9897e4f-972e-4b3e-9bff-8481e8ccd729; _gid=GA1.2.1160512539.1665666921',
   'referer': 'https://juejin.cn/'
}

data={
'cate_id': '"6809635626879549454"',
'cate_id': '"6809635626879549454"'
}

# post请求的参数 必须要进行编码

data=urllib.parse.urlencode(data).encode('utf-8')

# post请求的参数 是不会拼接在url的后面  二十需要放在请求对象定制的参数中
request=urllib.request.Request(url=url,data=data,headers=headers)

# 模拟浏览器向服务器发送请求
response= urllib.request.urlopen(request)

# 获取响应内容
content =response.read().decode('utf-8')

# 字符串--》json对象
import json
result =json.loads(content)
# 打印数据
print(result)
fp=open('掘金首页第一页.text','w',encoding='utf-8')
fp.write(content)
# def parse(self, response):
       
#         li_list = response.xpath('//div[@class="bang_list_box"]/ul/li')

#         for li in li_list:
#             title = li.xpath('.//div[@class="name"]/a/text()').extract_first()





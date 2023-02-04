


import urllib.request
import urllib.response

url = 'https://dianying.taobao.com/cityAction.json?activityId&_ksTS=1665585987395_108&jsoncallback=jsonp109&action=cityAction&n_s=new&event_submit_doGetAllRegion=true'


headers={
  
    'cookie':' cna=YImgG6QXanACAXeFB2q8QwlB; t=8f426a265649bec572d59223b14c19dc; cookie2=14309288f88562136862dd9fdfdfa83c; v=0; _tb_token_=f6fb73e9e3e41; xlly_s=1; isg=BJGRzw1jlubMYfqteLSa8QtloJ0r_gVw4kvMCXMmt9h3GrFsu0_VQBp8uO78Ep2o; tfstk=coACBwXopkqCtfcutMgZYncjWCfPZIo1SvspRc5tcUTbVgTCimPVcwNXElfPyN1..; l=eBMf9ihRTNYuLxD8BOfwhurza77O9IRAguPzaNbMiOCP_QfH59_AW6PPFB8MCnGVhsEwR3ux1zSeBeYBqn4jjqj4axom4xMmn',
    'referer': 'https://dianying.taobao.com/',
  
}


request = urllib.request.Request(url = url, headers = headers)

response = urllib.request.urlopen(request)

# 获取响应内容
content = response.read().decode('utf-8')

# split切割
content = content.split('(')[1].split(')')[0]


with open('解析 淘票票地区.json','w',encoding='utf-8')as fp:
    fp.write(content)

import json
import jsonpath

obj = json.load(open('解析 淘票票地区.json','r',encoding='utf-8'))

city_list = jsonpath.jsonpath(obj,'$..regionName')

print(city_list)
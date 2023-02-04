import imp
import urllib.request


url='https://fanyi.baidu.com/v2transapi?from=en&to=zh'

headers={
   
    'Accept':'*/*',
    # 'Accept-Encoding':' gzip, deflate, br',
    # 'Accept-Language':'zh-CN,zh;q=0.9',
    # 'Acs-Token':'1665212646250_1665285891326_sRPWxOPA5mLtL4IAnvG7fto/5SaBa7s0185quKFPcayoj8ogoUYL5DDB46LoOPX+P656XvsFa08wNJyQUCeHfXTNyleg9wRUGdjtI/zYGDGAp1fdMZ7kt8fLchdVVmjd1c1kFHb5/u1KjuV/qa+q0rJlDBysRRJpt/ajkCBy3iqiQJu4yRu8hKNl1VI1RwP0kiwTxFju1MmeCUk5zEEmSpCWf1TkMk2ivjRF8Q+K7fBJwZOcXrF4kwkOl7fdvZqquPXC59qmE4dwRDldv8+J1jsKrzffNBUQBv7he2kojO/H+NwfvI5eypOh+qNi5Tfe',
    # 'Connection':'keep-alive',
    # 'Content-Length':'135',
    # 'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie': 'PSTM=1662622317; BIDUPSID=520A21206F1859990476E4E7CD850E1F; BAIDUID=E54D2259991D8B1C10A995DC0B72EB00:FG=1; APPGUIDE_10_0_2=1; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; BDORZ=FFFB88E999055A3F8A630C64834BD6D0; H_PS_PSSID=; BAIDUID_BFESS=E54D2259991D8B1C10A995DC0B72EB00:FG=1; delPer=0; PSINO=6; BA_HECTOR=2ha10l2105812181a40g6pkk1hk4dq71a; ZFY=4eCPKRVfvglghvKPw8uLLKFS4od4AcMD5LN5wTc5s4M:C; BDRCVFR[AXKy_7ufun_]=mk3SLVN4HKm; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1663899722,1664180920,1665283919; ab_sr=1.0.1_Y2I1MDhhNzg4YWNjNDk2NmU0NGIwOGMxYTI1OTFlNDliMTNjNDA3NTVmMTUxNjM5ZTI1NDU5N2ZiY2RhM2U2MjhkOGY5ZTIzNGU4NmY0NTAwYjcxYzg4YjA5ODI0ODlmNGQwZGQ0MDI1Zjg5YTE4ZDJlMzczYzY5MjAxOTdjMWE4ZGZhYWE1OTk0MWFiMDFmNmFlYTA2NDk0Y2FkNjgzNw==; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1665285891',
    # 'Host':'fanyi.baidu.com',
    # 'Origin: https':'//fanyi.baidu.com',
    # 'Referer: https':'//fanyi.baidu.com/?aldtype=16047',
    # 'sec-ch-ua':' "Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
    # 'sec-ch-ua-mobile':'?0',
    # 'sec-ch-ua-platform':'"Windows"',
    # 'Sec-Fetch-Dest':'empty',
    # 'Sec-Fetch-Mode':'cors',
    # 'Sec-Fetch-Site':'same-origin',
    # 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
    # 'X-Requested-With':' XMLHttpRequest',
}

data={
    'from': 'en',
    'to': 'zh',
    'query': 'love',
    'simple_means_flag':'3',
    'sign': '198772.518981',
    'token':' 9b20fbc8f8816a855143a831bd893b14',
    'domain': 'common'
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
obj=json.loads(content)


# 打印数据
print(obj)

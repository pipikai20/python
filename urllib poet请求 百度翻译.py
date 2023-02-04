# post 请求
import imp
import urllib.request

url='https://fanyi.baidu.com/langdetect'

headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'}

data={
    'kw':'spider'
}
# post请求的参数 必须要进行编码

data=urllib.parse.urlencode(data).encode('utf-8')

# post请求的参数 是不会拼接在url的后面  需要放在请求对象定制的参数中
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


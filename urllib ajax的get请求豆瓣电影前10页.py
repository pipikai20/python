# https://movie.douban.com/j/chart/top_list?type=24&interval_id=100%3A90&action=&start=0&limit=20

# https://movie.douban.com/j/chart/top_list?type=24&interval_id=100%3A90&action=&start=20&limit=20

# https://movie.douban.com/j/chart/top_list?type=24&interval_id=100%3A90&action=&start=40&limit=20

# https://movie.douban.com/j/chart/top_list?type=24&interval_id=100%3A90&action=&start=60&limit=20

# page  1  2  3  4 
# start 0  20 40 60

# start=(page-1)*20

import imp
from urllib import request, response
import urllib.parse
import urllib.request

# 起始页码
def create_request():
    base_url ='https://movie.douban.com/j/chart/top_list?type=24&interval_id=100%3A90&action=&'

    data={
        'start':(page - 1)*20,
        'limit':20,
    }

    data= urllib.parse.urlencode(data)

    url = base_url+data
    print(url)

    headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'}

    request = urllib.request.Request(url=url,headers=headers)

    return request

# 获取数据
def get_content (requset):
    response= urllib.request.urlopen(request)
    content =response.read().decode('utf-8')
    return content

# 下载数据

def down_load(page,content):
    fp=open('豆瓣_'+str(page)+ '.json','w',encoding='utf-8')
    fp.write(content)


# 程序的入口
if __name__== '__main__':
    start_page= int(input('请输入起始的页码'))
    end_page= int(input('请输入结束的页码'))

    for page in range(start_page,end_page+1):
        # 每一页都有自己的请求对象的定制
         request=create_request()
        #  获取响应的数据
         content= get_content(request)
        # 下载
         down_load(page,content)

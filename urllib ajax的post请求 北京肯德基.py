# http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname
# post

# http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname

# http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname


import urllib.request
# base_url='http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname'


def create_request():
    base_url =' http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname'

    data={
    'cname': '北京',
    'pid': 'page',
    'Index': '3',
    'pageSize': '10'
    }

    
    data= urllib.parse.urlencode(data).encode('utf-8')

    headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'}

    request = urllib.request.Request(url=base_url,data=data,headers=headers)
    
    return request

# 获取数据
def get_content (requset):
    response= urllib.request.urlopen(request)
    content =response.read().decode('utf-8')
    return content

# 下载数据

def down_load(page,content):
    fp=open('肯德基北京_'+str(page)+ '.json','w',encoding='utf-8')
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



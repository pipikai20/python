# (1)请求对象的定制
# （2）获取网页的源码
# （3）下载


# 需求 下载的前三页的图片

# https://sc.chinaz.com/tupian/huacaotupian.html
# https://sc.chinaz.com/tupian/huacaotupian_2.html


from tkinter.tix import Tree
import urllib.request
from lxml import etree

def create_request(page):
    if(page== 1 ):
        url ='https://sc.chinaz.com/tupian/huacaotupian.html'
    else:
        url='https://sc.chinaz.com/tupian/huacaotupian_'+str(page) + '.html'



    headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'}

    request = urllib.request.Request(url=url,headers=headers)
    
    return request

# 获取数据
def get_content (requset):
    response= urllib.request.urlopen(request)
    content =response.read().decode('utf-8')
    return content

# 下载数据

def down_load(content):

    # 下载图片
    # urllib.request.urlretrieve('图片的地址i，'文件的名字')
    tree = etree.HTML(content)

    name_list = tree.xpath('//div[@class="container"]//img/@alt')

   

    # 一般涉及到图片的网站都会懒加载 
    src_list = tree.xpath('//div[@class="container"]//img/@data-original')

    for i in range(len(name_list)):
        name = name_list[i]
        src = src_list[i]
        url= 'https:' + src

        print(name,src)

        urllib.request.urlretrieve(url=url,filename = '解析 站长素材 图片 img' + name + '.jpg')


# 程序的入口
if __name__== '__main__':
    start_page= int(input('请输入起始的页码'))
    end_page= int(input('请输入结束的页码'))

    for page in range(start_page,end_page+1):

        # 每一页都有自己的请求对象的定制
         request=create_request(page)

        #  获取响应的数据
         content= get_content(request)

        # 下载
         down_load(content)


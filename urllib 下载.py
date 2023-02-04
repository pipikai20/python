import imp
import urllib.request


# 下载网页
url_page = 'https://www.baidu.com'


# url代表的是下载的路径 filename文件的名字
# python中可以变量是名字 也可以直接写值
urllib.request.urlretrieve(url_page,'baidu.html')



# 下载图片
url_img = 'https://img2.baidu.com/it/u=4226151860,2032058341&fm=253&fmt=auto&app=138&f=JPEG?w=281&h=499'

urllib.request.urlretrieve(url=url_img,filename='karry.jpg')


# 下载视频
url_video='blob:https://haokan.baidu.com/cc881bd5-7b53-49fd-aaca-fd3b6c878766'

urllib.request.urlretrieve(url_video,'karry2.mp4')

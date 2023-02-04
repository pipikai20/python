# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from fileinput import filename

from itemadapter import ItemAdapter


# 如果想使用管道的话 那么就需要
class DangdangScrapyPipeline:
    def open_spider(self,spider):
         self.fp=open('book.json','w',encoding='utf-8')
    # item就是yield后面的book对象
    def process_item(self, item, spider):
       

        # (1)write方法必须写一个字符串 str（）强转
        # （2）w模式 会每一个对象打开一次文件 覆盖之前的内容 要用a模式


        self.fp.write(str(item))

        # with open ('book.json','a',encoding='utf-8')as fp:
        #     fp.write(str(item))


        return item

        def close_spiders(self,spider):
            self.fp.close()

import urllib.request

# 多条管道下载
# (1)定义管道 
# (2)在setting中开启管道  'dangdang_scrapy.pipelines.DangdangScrapyPipeline': 301

class DangdangScrapyPipeline:
    def process_item(self,item,spider):

        url ='http:' + item.get('src')
        filename='./books/' + item.get('name') + '.jpg'

        urllib.request.urlretrieve(url=url,filename=filename)

        return item


        
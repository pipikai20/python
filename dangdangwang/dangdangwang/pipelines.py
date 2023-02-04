# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import pymysql


class DangdangwangPipeline:
    def __init__(self):
        self.connect = pymysql.connect(host="localhost", user="root", passwd="123456", db="dangdangwang")
        self.cursor = self.connect.cursor()
        print("数据库连接成功")

    def process_item(self, item, spider):
        print("开始保存数据")

        insertsql = "insert into dangdang(name,price,title,author,press,comment,content,btime) values (%s,%s,%s,%s,%s,%s,%s,%s)"

        self.cursor.execute(insertsql, (
            item['name'], item['price'], item['title'], item['author'], item['press'],
            item['comment'], item['content'] ,item['btime']))

        self.connect.commit()

        print("保存数据成功")

        return item

    def parse_close(self):
        self.connect.close()
        self.cursor.close()


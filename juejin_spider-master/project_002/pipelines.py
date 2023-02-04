# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

class Project002Pipeline(object):

    def __init__(self):
        db = {
            'host': 'localhost',
            'port': 3306,
            'user': 'root',
            'password': '123456',
            'database': 'juejin',
        }
        self.conn = pymysql.connect(**db)
        self.cursor = self.conn.cursor()
        self._sql = None


    
    def process_item(self, item, spider):
        print(item)
        self.cursor.execute("""INSERT IGNORE INTO juejin (id,title,`url`,`likes`,content,category,users,updated_date,article_id) 
        VALUES (null,%s,%s,%s,%s,%s,%s,%s,%s)""", 
                    (item['title'], 
                    item['url'], 
                    item['likes'], item['content'], item['category'], item['users'], 
                    item['updated_date'],
                    item['article_id']
                    )
                )            
        self.conn.commit()

    # def process_item(self, item, spider):
    #     return item

# -*- coding: utf-8 -*-
import scrapy
import json
from project_002.items import Project002Item

class JuejinSpider(scrapy.Spider):
    name = 'juejin'
    allowed_domains = ['www.juejin.cn']
    start_urls = ['https://api.juejin.cn/recommend_api/v1/article/recommend_all_feed?aid=2608&uuid=7140909935034779176&spider=0']

    info = {"id_type": 2, "client_type": 2608, "sort_type": 200, "cursor": "0", "limit": 20}
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36',
}
#  标记是否有更多数据
    has_more = True

# 利用set 取一下重
    dataSet = set()
# 存储数据的列表
    dataList = []
    def parse(self, response):
        pass

    def parse_item(self, response):
        print('进入此步骤,响应为')
        item = Project002Item()
        edges = json.loads(response.text)['data']['articleFeed']['items']['edges']
        temp = []
        for edge in edges:
            node = edge['node']
            temp.append({"title": node['title'], "url": node['originalUrl'], "likes": node['likeCount'], 'content': node['content'], 'users': node['user']['username'], 'updated_date': node['updatedAt'], 'category': node['category']['name'], 'article_id': node['id']})
        item = temp
        return item

    def start_requests(self):
        url = 'https://web-api.juejin.im/query'
        query_date = {"operationName":"","query":"","variables":{"first":100,"after":"","order":"MONTHLY_HOTTEST"},"extensions":{"query":{"id":"21207e9ddb1de777adeaca7a2fb38030"}}}
        response = scrapy.Request(url, method="POST",headers=self.headers, body=json.dumps(query_date),callback=self.parse_item)
        yield response

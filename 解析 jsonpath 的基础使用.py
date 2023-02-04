# https://blog.csdn.net/luxideyao/article/details/77802389    这是教程

import json
import jsonpath

obj = json.load(open('解析 jsonpath例子.json','r',encoding='utf-8'))

# 书店所有书的作者
anthor_list1 = jsonpath.jsonpath(obj,'$.store.book[*].author')
print(anthor_list1)

# 所有的作者
anthor_list2 = jsonpath.jsonpath(obj,'$..author')
print(anthor_list2)

# store 下面所有的元素
anthor_list3 = jsonpath.jsonpath(obj,'$.store.*')
print(anthor_list3)

# store里面所有东西的price
anthor_list4 = jsonpath.jsonpath(obj,'$.store..price')
print(anthor_list4)

# 第三个书
anthor_list5 = jsonpath.jsonpath(obj,'$..book[2]')
print(anthor_list5)


# 最后一本书
anthor_list6 = jsonpath.jsonpath(obj,'$..book[(@.length-1)]')
print(anthor_list6)


# 前面两本书
anthor_list7 = jsonpath.jsonpath(obj,'$..book[0,1]')   
# anthor_list7 = jsonpath.jsonpath(obj,'$..book[:2]') 
print(anthor_list7)


# 过滤出所有的包含isbn的书
anthor_list8 = jsonpath.jsonpath(obj,'$..book[?(@.isbn)]')
print(anthor_list8)

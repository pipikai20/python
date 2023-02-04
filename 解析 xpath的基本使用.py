from lxml import etree

# xpath解析    
# （1）本地文件      etree.parse
# （2）服务器响应的数据   response.read().decode('utf-8')      etree.HTML()


# xpath解析本地文件
tree = etree.parse('解析 xpath的基本使用.html')

# 查找ul下面的li
li_list1 = tree.xpath('//body/ul/li')

# 判断列表的长度

print(li_list1)
print(len(li_list1))


# 查找所有有id属性的li标签  text()获取标签中的内容
li_list2 = tree.xpath('//ul/li[@id]/text()')

print(li_list2)
print(len(li_list2))

# 查找id为l1的li标签  注意引号问题
li= tree.xpath('//ul/li[@id="l1"]/@class')

print(li)
print(len(li))

# 查找id中包含l的li标签
li_list3 = tree.xpath('//ul/li[contains(@id,"l")]/text()')
print(li_list3)
print(len(li_list3))

# 查找id的值以l开头的li标签
li_list4 = tree.xpath('//ul/li[starts-with(@id,"l")]/text()')
print(li_list4)
print(len(li_list4))










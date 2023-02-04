# import sys
# import re

# str = "东野圭吾：白夜行（易烊千玺、孟非推荐，东野圭吾作品无冕之王）"+"）"
# result = re.sub(u"\\（.*?）|\\{.*?}|\\[.*?]|\\【.*?】|\\.*?）", "", str.encode('utf-8').decode())
# print(result)

import re
string = "'2020-07-01': 6, '2021-10-01': 4"
p1 = re.compile(r'["](.*?)["]', re.S)  #最小匹配
p2 = re.compile(r'[(](.*)[)]', re.S)   #贪婪匹配
print(re.findall(p1, string))
print(re.findall(p2, string))
import csv
file = open(r'C:\Users\皮皮凯\Desktop\py基础\dangdang2.csv', encoding='utf-8')
fileReader = csv.reader(file)
filedata = list(fileReader)
data = []

for i in filedata:
    # 数据表第四列为出版社
    t = i[8:9]
    data.append(''.join(t))

# 去重
punlish_Number = len(set(data))
print('出版社共'+str(punlish_Number)+'个')
punlish_data = list(set(data))

# 统计出版社
dict = {}
for i in data:
    dict[i] = dict.get(i,0)+1
# 输出所有的出版社以及个数
print(dict)
# print(len(dict))


import pandas as pd
# 读取文件
df = pd.read_csv(r'C:\Users\皮皮凯\Desktop\py基础\dangdang2.csv')
# 对价格列进行操作
index = df['comment'].notnull()
df = df[index]
df.to_csv(r'C:\Users\皮皮凯\Desktop\py基础\dangdang3.csv')




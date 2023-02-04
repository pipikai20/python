import csv
file = open(r'C:\Users\皮皮凯\Desktop\py基础\dangdang2.csv', encoding='utf-8')
fileReader = csv.reader(file)
filedata = list(fileReader)
data = []

for i in filedata:
    
    t = i[11:12]
    data.append(''.join(t))

# 去重
punlish_Number = len(set(data))
print('出版时间'+str(punlish_Number)+'个')
punlish_data = list(set(data))

dict = {}
for i in data:
    dict[i] = dict.get(i,0)+1

print(dict)
# print(len(dict))




import matplotlib.pyplot as plt
import numpy as np

# 定义数据
x = '2022-07-01', '2022-09-01', '2022-06-01',  '2022-08-01',  '2022-09-30', '2022-04-01', '2022-03-01', '2022-07-26','2022-01-14', '2022-08-31','2022-01-18',  '2022-05-31', '2022-01-05','2022-09-15', '2022-05-01', '2022-02-01', '2022-08-30', '2022-04-13'
y = [13,3,4,8,2,6,3,1,1,1,1,2,1,1,2,1,1,1] # 用自定义关系确定y的值

# 绘图
# 1. 确定画布
fig=plt.figure(figsize=(9,5))  # figsize:确定画布大小 

# 2. 绘图
plt.scatter(x,  # 横坐标
            y,  # 纵坐标
            c='red',  # 点的颜色
            label='出版书籍个数')  # 标签 即为点代表的意思
# 3.展示图形
plt.legend()  # 显示图例

fig.autofmt_xdate()
plt.show()  # 显示所绘图形

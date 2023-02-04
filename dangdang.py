import csv
file = open(r'C:\Users\皮皮凯\Desktop\py基础\dangdang2.csv', encoding='utf-8')
fileReader = csv.reader(file)
filedata = list(fileReader)
data = []

for i in filedata:
    # 数据表第四列为出版社
    t = i[11:12]
    data.append(''.join(t))

# 去重
punlish_Number = len(set(data))
print('出版时间'+str(punlish_Number)+'个')
punlish_data = list(set(data))
# 统计出版社
dict = {}
for i in data:
    dict[i] = dict.get(i,0)+1
# 输出所有的出版社以及个数
print(dict)
# print(len(dict))



# 导入我们所需的库 as：即给库取别名，方便书写
import matplotlib.pyplot as plt
import numpy as np

# 定义数据
x = '2022-07-01', '2022-09-01', 
 
y = [13,3] # 用自定义关系确定y的值

# 绘图
# 1. 确定画布
fig=plt.figure(figsize=(8, 4))  # figsize:确定画布大小 

# 2. 绘图
plt.scatter(x,  # 横坐标
            y,  # 纵坐标
            c='red',  # 点的颜色
            label='function')  # 标签 即为点代表的意思
# 3.展示图形
plt.legend()  # 显示图例
fig.autofmt_xdate()
plt.show()  # 显示所绘图形

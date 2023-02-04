import csv
file1 = open(r'C:\Users\皮皮凯\Desktop\py基础\dangdang2.csv',encoding='utf-8')
fileReaders = csv.reader(file1)
filedatas = list(fileReaders)
#print(filedatas)
data3 = []
data4 = []
for i in filedatas:

    t = i[9]

    data3.append(''.join(t))
a = data3[1:10]

for i in filedatas:

    t = i[4]

    data4.append(''.join(t))
b = data4[1:10]


import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
pubs = b
book_number = a
plt.barh(pubs, book_number)  # 横放条形图函数 barh
plt.title('当当Python图书评论前十')
plt.show()





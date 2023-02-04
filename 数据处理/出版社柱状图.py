import matplotlib.pyplot as plt

# 设置中文显示
plt.rcParams['font.sans-serif'] = 'SimHei'
plt.rcParams['axes.unicode_minus'] = False

num_list = [9, 9, 8, 11,9,19,10,9,10,13,9,18]
name_list = ['中国友谊出版公司', '青岛出版社', '天津人民出版社', '北京十月文艺出版社', '浙江文艺出版社','北京联合出版有限公司',
  '湖南文艺出版社','南海出版公司', '海豚出版社',  '人民文学出版社', '时代文艺出版社' ,'中信出版社']
plt.barh(range(len(num_list)),
        num_list,
        align="center",
        # 设置标签
        tick_label=name_list,)
plt.title('出版社前十柱状图')
plt.show()

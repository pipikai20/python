import matplotlib.pyplot as plt
# 设置中文显示
plt.rcParams['font.sans-serif'] = 'SimHei'
plt.rcParams['axes.unicode_minus'] = False
labels = '0-40元','40-70元','70-100元','100元以上'
fraces = [147,170,12,33]
# 使画出来的图形为标准圆
plt.axes(aspect=1)
# 突出分离出数量最多的第二部分
explode = [0, 0, 0,0]
colors = ['skyblue', 'pink', 'yellow','green']
plt.pie(x=fraces,
        labels=labels,
        colors=colors,
        # 显示比例
        autopct='%0f%%',
        explode=explode,
        # 显示阴影，使图形更加美观
        shadow=True)
plt.show()



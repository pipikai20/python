import pymysql
from pyecharts.charts import Bar, Pie, Line
import pyecharts.options as opts



def select_geju_jiage():
    conn = pymysql.connect(
        host='localhost', 
        user='root',
        password='123456',
        db='dangdangwang',
        port=3306,
        autocommit=False,
        charset='utf8mb4')

    cur = conn.cursor()

    select_sql = "SELECT NAME,SUM(COMMENT) FROM dangdang GROUP BY NAME;"

    cur.execute(select_sql)

    result1 = cur.fetchall()

    print(result1)
    name = []
    comment = []

    for i in result1:
        name.append(i[0])
        comment.append(int(i[1]))

    return name, comment


def zhuzhuangtu():  # 柱状图
    name, comment = select_geju_jiage()
    bar = Bar(init_opts=opts.InitOpts(width='1000px', height='600px'))
    bar.add_xaxis(name)
    bar.add_yaxis("销量", comment)
    bar.set_global_opts(title_opts=opts.TitleOpts("各图书销量统计"))
    bar.set_series_opts(label_opts=opts.LabelOpts(position="top"))
    bar.render("柱状图.html")


if __name__ == '__main__':
    zhuzhuangtu()



def meiguitu():
    name, comment = select_geju_jiage()
    pie = Pie()

    pie.add("", [list(z) for z in zip(name, comment)], radius=["40%", "70%"], rosetype="area")

    pie.set_global_opts(title_opts=opts.TitleOpts(title="各类图书销量比例"))

    pie.set_series_opts(label_opts=opts.LabelOpts(formatter="{b}:{c}"))
    pie.render("玫瑰图.html")


if __name__ == '__main__':
    meiguitu()

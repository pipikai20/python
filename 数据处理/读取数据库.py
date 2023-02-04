
import pymysql
import csv
 
def from_mysql_get_all_info():
    conn = pymysql.connect(
       host='localhost', 
        user='root',
        password='123456',
        db='dangdangwang',
        port=3306,
        autocommit=False,
        charset='utf8mb4')
    cursor = conn.cursor()
    sql = 'select * from dangdang'
    cursor.execute(sql.encode('utf-8'))
    data = cursor.fetchall()
    conn.close()
    return data
 
 
def write_csv():
    data = from_mysql_get_all_info()
    filename = 'dangdangwang.csv'#文件名和路径
    with open(filename,mode='w',encoding='utf-8') as f:
        write = csv.writer(f,dialect='excel')
        for item in data:
            write.writerow(item)
 
write_csv()





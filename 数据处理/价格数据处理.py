import os

import csv

file = open(r'C:\Users\皮皮凯\Desktop\py基础\dangdang.csv',encoding='utf-8')

fileReader = csv.reader(file)

filedata = list(fileReader)

data=[]

s1=[]

s2=[]

s3=[]

s4=[]

for i in filedata:

    t=i[4]

    data.append(''.join(t))

print(data)

for j in range(361):
             
    if float(data[j]) >40.0:

        s1.append(data[j])

    if float(data[j]) >70.0:

        s2.append(data[j])

    elif float(data[j]) > 100.0:

        s3.append(data[j])

    else:

        s4.append(data[j])

print(len(s1))

print(len(s2))

print(len(s3))

print(len(s4))

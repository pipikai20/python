import csv

import matplotlib.pyplot as plt

import numpy as np

from sklearn.cluster import KMeans

file1 = open(r'C:\Users\皮皮凯\Desktop\py基础\dangdang2.csv',encoding='utf-8')

fileReaders = csv.reader(file1)

filedatas = list(fileReaders)

print(filedatas)

g=[]

for i in filedatas:

    t=i[2]

    g.append(''.join(t))

X=np.array(g[1:10]).reshape(-1, 1)

print(X)

km2 = KMeans(n_clusters=2).fit(X)

print("当k=2时聚类结果:", km2.labels_)

import pymysql
import pandas as pda
import numpy as npy
from sklearn.decomposition import PCA
import matplotlib.pylab as pyl

conn = pymysql.connect(host='localhost', user='root', password='Zwp0816...', db='jd_goods')
sql = 'SELECT * FROM new_goods'

data = pda.read_sql(sql, conn)
#data['价格'][(data['价格'] < 1500)] = None
ch = data['评论'] / data['价格']
data['评点比'] = ch
data2 = pda.DataFrame()
data2.insert(0, '价格', data.pop('价格'))
data2.insert(1, '评论', data.pop('评论'))
data2.insert(2, '评价比', ch)
#print(data)
pca = PCA()

pca.fit(data2)
Char = pca.components_
#print(Char)

pca2 = PCA(2)
pca2.fit(data2)
dimRed = pca2.transform(data2)
#print(pca2.components_)
pyl.scatter(dimRed[:, 0], dimRed[:, 1], alpha=0.5, edgecolors='white')
pyl.show()
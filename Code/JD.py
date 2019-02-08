import pandas as pd
import matplotlib.pylab as pyl
import numpy as npy 

print("正在读取数据...")
data = pd.read_excel("D:/文件/学习/Python/数据挖掘与分析/我的数据/2018.8月下旬京东笔记本电脑信息20000+.xlsx")
print("读取成功!")
print(data.describe())
data2 = data.T
x1 = data2.values[1]
y1 = data2.values[2]

pyl.title("show")
pyl.xlabel("Price")
pyl.ylabel("Comments")
pyl.xlim(0, 50000)
#pyl.ylim(0, 100000)
pyl.scatter(x1, y1, alpha=0.5, c='c')
pyl.show()

data['价格'][(data['价格']<1500)] = None
data = data.dropna()
data3 = data.T
price_max = data3.values[1].max()
price_min = data3.values[1].min()
comment_max = data3.values[2].max()
comment_min = data3.values[2].min()
price_rg = price_max - price_min
comment_rg = comment_max - comment_min
price_dst = round(price_rg / 12)
comment_dst = comment_rg / 12

price_sty = npy.arange(price_min,price_max,price_dst)
print(price_sty)
pyl.hist(data3.values[1], price_sty)
pyl.show()

comment_sty = npy.arange(comment_min,comment_max,comment_dst)
pyl.hist(data3.values[2], comment_sty)
pyl.show()


import jieba
import jieba.analyse

with open(r'D:\文件\学习\Python\数据挖掘与分析\我的数据\douluodalu.txt', 'r', encoding='utf-8') as f:
    data = f.read()
result = jieba.analyse.extract_tags(data)
print(result)

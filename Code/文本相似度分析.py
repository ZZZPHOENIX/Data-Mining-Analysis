from gensim import corpora, models, similarities
import jieba
from collections import defaultdict

#读取文档
print("\n正在读取文档...")
doc1 = r"D:\文件\学习\Python\数据挖掘与分析\我的数据\douluodalu.txt"
doc2 = r"D:\文件\学习\Python\数据挖掘与分析\我的数据\jueshitangmen.txt"
data1 = open(doc1, encoding='utf-8').read()
data2 = open(doc2, encoding='utf-8').read()
print("...读取完成")

#文档分词
print("\n正在对文档分词...")
data1 = jieba.cut(data1)
data2 = jieba.cut(data2)
print("...分词完成")

#文档词语处理
print("\n正在对文档词语进行处理...")
wordList1 = ''
wordList2 = ''
for item in data1:
    wordList1 += item + ' '
for item in data2:
    wordList2 += item + ' '
wordLists = [wordList1, wordList2]
wordLists = [[word for word in wordList.split()] for wordList in wordLists]
print("...处理完成")

#词频统计
print("\n正在进行词频统计...")
frequency = defaultdict(int)
for words in wordLists:
    for word in words:
        frequency[word] += 1
print("...统计完成")

#词汇过滤
print("\n正在进行词汇过滤...")
wordList = [[word for word in words if frequency[word] > 10] for words in wordLists]
print("...过滤完成")

#建立词典
print("\n正在建立词典...")
dic = corpora.Dictionary(wordLists)
dic.save(r"D:\文件\学习\Python\数据挖掘与分析\我的数据\dictionary.txt")
print("...建立完成")

#读取目标文件并建立新的语料库
print("\n正在读取目标文件并建立新的语料库...")
doc3 = r"D:\文件\学习\Python\数据挖掘与分析\我的数据\longwangchuanshuo.txt"
data3 = open(doc3, encoding='utf-8').read()
data3 = jieba.cut(data3)
wordList3 = ''
for item in data3:
    wordList3 += item + ' '
newWordList = wordList3
newDic = dic.doc2bow(newWordList.split())
corpus = [dic.doc2bow(words) for words in wordLists]
tfidf = models.TfidfModel(corpus)
featureNum = len(dic.token2id.keys())
index = similarities.SparseMatrixSimilarity(tfidf[corpus], num_features=featureNum)
sim = index[tfidf[newDic]]
print(sim)
print("...操作完成")

#
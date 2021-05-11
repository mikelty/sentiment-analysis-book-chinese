# -*- coding: utf-8 -*-
import jieba.analyse as analyse
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from time import perf_counter
from icecream import ic
import os
import jieba

start_time=perf_counter()

def load_stopwords():
    stopwords=set()
    os.chdir('.\\stopwords')
    for fn in os.listdir():
        if fn[-3:]=='txt':
            with open(fn,'r') as fp:
                for word in fp.readlines():
                    stopwords.add(word.strip())
    return stopwords


with open('.\\tz.txt','r') as fp:
    text =''.join(fp.readlines())

stopwords =load_stopwords()
# jieba.cut直接得到generator形式的分词结果
seg = jieba.cut(text)
seg=list(seg)
newseg=[word for word in seg if word not in stopwords]
ic(len(newseg))

# TF-IDF
tf_result = analyse.extract_tags(text, topK=10)
ic('tfidf')
ic(tf_result)
# TextRank
ic('textrank')
tr_result = analyse.textrank(text, topK=10)
ic(tr_result)
wc=WordCloud(width = 800, height = 800,
             background_color ='white',
             min_font_size = 10,
             stopwords=stopwords,
             font_path=r'C:\Windows\Fonts\STHUPO.ttf').generate(' '.join(newseg))

#解决中文显示问题
plt.rcParams['font.sans-serif'] = ['KaiTi'] # 指定默认字体
plt.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题
plt.figure(figsize=(8, 8), facecolor=None)
plt.imshow(wc)
plt.axis("off")
plt.tight_layout(pad=0)
ic(perf_counter() - start_time)
plt.show()
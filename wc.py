# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
from wordcloud import WordCloud

words =['征战', '四海', '只', '为', '今日', '一胜', '，', '我', '不会', '再败', '了', '。']

wc=WordCloud(width = 800, height = 800,
                background_color ='white',
                min_font_size = 10,
             font_path=r'C:\Windows\Fonts\STHUPO.ttf').generate(' '.join(words))

#解决中文显示问题
plt.rcParams['font.sans-serif'] = ['KaiTi'] # 指定默认字体
plt.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题
plt.figure(figsize=(8, 8), facecolor=None)
plt.imshow(wc)
plt.axis("off")
plt.tight_layout(pad=0)

plt.show()
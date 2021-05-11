import matplotlib.pyplot as plt
import pickle
from icecream import ic
from snownlp import SnowNLP
from tqdm import tqdm

with open('.\\tz.txt','r') as fp:
    text =''.join(fp.readlines())

text = SnowNLP(text)
sent = text.sentences
res=[]
for sen in tqdm(sent):
    s = SnowNLP(sen)
    res.append(s.sentiments)
    
with open('sentres.pickle','wb') as fp:
    pickle.dump(res,fp)

plt.hist(res,30)
plt.show()

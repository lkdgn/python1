import jieba
s = '陈海升（队长）(2015034643038)：代码测试员。风格多变，擅长多种语言的”helloworld“编程，兴趣是下一门语言的“helloworld”。宣言是：学习没有期限，如果有，那就把它删掉。'
s1='艾晓晗(2015034643010)：项目经理。风格俏皮可爱，擅长统筹规划，兴趣广泛。宣言是：好好学习。'
s2='詹振根(2015034643021)：代码编写员。风格哲学，擅长在团队项目中carry，当大哥。对哲学和python很有兴趣。 宣言是：python python Michael Jackson。'
s3='黄志明(2015034643001)：ui设计。风格随性自然，擅长matlab；对数据挖掘、matlab很有兴趣。宣言是：做平凡的事，当不平凡的人。'
m=s+s1+s2+s3
cut = jieba.cut(m)
from collections import Counter
c = Counter(cut)
l3=' ，。、？》《；：‘“’”、|】}【{,./<>?:"\|[]{}-=_+)(*&^%$#@!~`'
for key,value in list(c.items()):
    a1=key
    b1=l3.find(a1)
    c1=value
    if b1!=-1:
        del c[key]
    if c1==1:
        del c[key]
print(c)
l1=[]
l2=[]
for key,value in c.items():
    l1.append(key)
    l2.append(value)
from pylab import mpl
mpl.rcParams['font.sans-serif'] = ['SimHei']
import matplotlib.pyplot as plt
plt.bar(l1,l2)
plt.show()
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
fig = plt.figure()
plt.pie(l2, labels=l1, autopct='%1.2f%%')
plt.show()
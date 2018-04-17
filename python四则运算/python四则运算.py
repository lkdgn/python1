import tkinter
import random
from fractions import Fraction

m=['+','-','×','÷']
nn='0'

window = tkinter.Tk()
window.title('四则运算')
window.geometry('300x150')
m1=tkinter.StringVar()
m1.set('')
m2=tkinter.StringVar()
m2.set('')
m3=tkinter.StringVar()
m3.set('')
m4=tkinter.StringVar()
m4.set('')
name=tkinter.Label(text='算式:',justify=tkinter.RIGHT,width=80)
name.place(x=5,y=5,width=80,height=20)
m1name=tkinter.Label(width=80,textvariable=m1)
m1name.place(x=60,y=5,width=80,height=20)
en=tkinter.Entry(width=80,textvariable=m3)
en.place(x=180,y=5,width=80,height=20)
name2=tkinter.Label(text='结果:',justify=tkinter.RIGHT,width=80)
name2.place(x=5,y=30,width=80,height=20)
m2name=tkinter.Label(width=80,textvariable=m2)
m2name.place(x=60,y=30,width=80,height=20)
name3=tkinter.Label(text='答案:',justify=tkinter.RIGHT,width=80)
name3.place(x=5,y=60,width=80,height=20)
m4name=tkinter.Label(width=80,textvariable=m4)
m4name.place(x=75,y=60,width=50,height=20)

def s():
    b['text']='下一题'
    b2['text'] = '真分数'
    m1.set('')
    m2.set('')
    m3.set('')
    m4.set('')
    mm = f()
    a = mm
    def g(a):
        nn = en.get()
        if str(nn) == str(mm):
            m2.set('正确')
        else:
            m2.set('错误')
            m4.set(mm)
    en.bind('<Key-Return>', g)
def s1():
    b['text'] = '整数'
    b2['text']='下一题'
    m1.set('')
    m2.set('')
    m3.set('')
    m4.set('')
    mm = f2()
    a=mm
    def g(a):
        nn = en.get()
        if str(nn) == str(mm):
            m2.set('正确')
        else:
            m2.set('错误')
            m4.set(mm)
    en.bind('<Key-Return>', g)

def s2():
    window.destroy()
b=tkinter.Button(text='整数',command=s)
b.place(x=60,y=90,width=50,height=20)
b2=tkinter.Button(text='真分数',command=s1)
b2.place(x=120,y=90,width=50,height=20)
b1=tkinter.Button(text='关闭',command=s2)
b1.place(x=180,y=90,width=50,height=20)

def f():
    f=random.randint(0,3)
    n1=random.randint(1,10)
    n2=random.randint(1,10)
    r = 0
    if f==0:
        r=n1+n2
    elif f==1:
        n1,n2=max(n1,n2),min(n1,n2)
        r=n1-n2
    elif f==2:
        r=n1*n2
    elif f==3:
        if n1==n2:
            r=1
        else:
            n1, n2 = max(n1, n2), min(n1, n2)
            if n2==1:
                r=n1
            else:
                while n1 % n2 != 0:
                    n1 = random.randint(1, 10)
                    n2 = random.randint(1, 10)
                    n1, n2 = max(n1, n2), min(n1, n2)
                    r = int(n1 / n2)
    a=str(n1)+str(m[f])+str(n2)+'='
    m1.set(a)
    return r

def f2():
    q = []
    f = random.randint(0, 3)
    t1 = random.randint(0, 20)
    t2 = random.randint(t1, 20)
    a = Fraction(t1, t2)
    t1 = random.randint(0, 20)
    t2 = random.randint(t1, 20)
    b = Fraction(t1, t2)
    if f==0:  # 加法
        q.append(a + b)
        q.append(str(a)+m[f]+str(b))
        m1.set(q[1])
        return q[0]
    elif f==1:  # 减法
        if a < b:
            tm = a
            a = b
            b = tm
        q.append(a - b)
        q.append(str(a) + m[f] + str(b))
        m1.set(q[1])
        return q[0]
    elif f==2:  # 乘法
        q.append(a * b)
        q.append(str(a) + m[f] + str(b))
        m1.set(q[1])
        return q[0]
    else:  # 除法
        c = Fraction(a, b)
        q.append(str(c))
        q.append(str(a) + m[f] + str(b))
        m1.set(q[1])
        return q[0]

window.mainloop()
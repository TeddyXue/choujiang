import tkinter as tk
from tkinter import *
import random

root=tk.Tk()
root.title('抽奖')
root.geometry('300x300')
boluo = tk.PhotoImage(file="./material/boluo.gif")#file：t图片路径
boluomi = tk.PhotoImage(file="./material/boluomi.gif")#file：t图片路径
liulian = tk.PhotoImage(file="./material/liulian.gif")#file：t图片路径
lizhi = tk.PhotoImage(file="./material/lizhi.gif")#file：t图片路径
pingguo = tk.PhotoImage(file="./material/pingguo.gif")#file：t图片路径
putao = tk.PhotoImage(file="./material/putao.gif")#file：t图片路径
xiangjiao = tk.PhotoImage(file="./material/xiangjiao.gif")#file：t图片路径
xigua = tk.PhotoImage(file="./material/xigua.gif")#file：t图片路径
list=[boluo,boluomi,liulian,lizhi,pingguo,putao,xiangjiao,xigua]
pic=random.choice(list)
switch=0
def random_pic():
    global switch
    if switch==0:
        label.config(image=random.choice(list))
        label.after(50,random_pic)
    else:
        if switch==15:
            label.config(image=random.choice(list))
            label['text']='中奖'

        else:
            delay=50*switch
            label.config(image=random.choice(list))
            label.after(delay, random_pic)
            switch+=1

def destroy():
    global switch
    switch+=1



label=tk.Label(root,image=pic,text='123')

button=tk.Button(root,text='stop',width=25,command=destroy)
button.pack(side='bottom')
random_pic()
label.pack()
root.mainloop()
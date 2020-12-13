# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 17:12:13 2020

@author: 29395
"""
#导入TK模块
import itertools
import allgameSurface
from allgameSurface import list_hard
import os
import random
import tkinter as tk
from PIL import Image,ImageTk
import math
import tkinter.messagebox
#窗口变量

def main():

    window = tk.Tk()

    # top = tkinter.Tk()
    #窗口标题
    window.title('24点')
    #窗口大小
    window.geometry('800x768')
    #画布大小设置，白色背景1024*768

    canvas = tk.Canvas(window, bg='white', height=768, width=1024)
    canvas.pack()
    path=os.getcwd()
    print(path)
    IMG=[]
    for i in range(1,13):
        im=Image.open(r'./pic/'+str(i)+'.png')
        img=ImageTk.PhotoImage(im)
        IMG.append(img)
    # print(len(IMG))
    numbers = list(range(0, 11))
    num_list = random.sample(numbers, 4)
    num_list2=[]
    for i in num_list:
        num_list2.append(i+1)
    print(num_list2)

    label = tk.Label(window, image=IMG[num_list[0]])
    label.place(x=0, y=100)
    label2 = tk.Label(window, image=IMG[num_list[1]])
    label2.place(x=200, y=100)
    label3 = tk.Label(window, image=IMG[num_list[2]])
    label3.place(x=400, y=100)
    label4 = tk.Label(window, image=IMG[num_list[3]])
    label4.place(x=600, y=100)
    def start():
        tkinter.messagebox.showinfo(title='游戏规则', message='欢迎来到24点小游戏。K=13,Q=12,j=11')

        tk.Label(window,text='输入算式:', font=('Arial49', 14)).place(x=10, y=500)

        #输入算式
        var_usr_name = tk.StringVar()
        entry_usr_name = tk.Entry(window, textvariable=var_usr_name, font=('Arial49', 14))
        entry_usr_name.place(x=120, y=500)

        var_usr_name2 = tk.StringVar()
        # 答案
        entry_usr_name1 = tk.Entry(window, textvariable=var_usr_name2, font=('Arial49', 14))
        entry_usr_name1.place(x=400, y=500)

        # #生命值
        # tk.Label(window, text='初始分数:', font=('Arial', 14)).place(x=10, y=600)
        # var_usr_name3 = tk.StringVar()
        # var_usr_name3.set(0)
        # entry_usr_name3 = tk.Entry(window, textvariable=var_usr_name3, font=('Arial', 14))
        # entry_usr_name3.place(x=120, y=600)

        def Suanfa():
              user = entry_usr_name.get()  # 获取文本框内容
              # num2=entry_usr_name3.get()
              user=eval(user)
              print(user)
              var_usr_name2 = tk.StringVar()
              var_usr_name2.set(user)
              # 答案
              entry_usr_name1 = tk.Entry(window, textvariable=var_usr_name2, font=('Arial49', 14))
              entry_usr_name1.place(x=400, y=500)
              if user >= 24:
                # 所得分数
                strnull = []
                tkinter.messagebox.showinfo(title='Hi', message='回答正确,游戏结束')
                window.destroy()
                list_hard[5] = user
                allgameSurface.next_screen(strnull,6)
                # var_usr_name3.set(int(num2)-1)
              elif user >= 24.0:
                strnull = []
                tkinter.messagebox.showinfo(title='Hi', message='回答正确,游戏结束')
                window.destroy()
                list_hard[5] = user
                allgameSurface.next_screen(strnull,6)

              else:
                # 所得分数
                tkinter.messagebox.showinfo(title='Hi', message='回答错误,游戏结束')
                window.destroy()
                allgameSurface.lose_screen(5)
                # var_usr_name3.set(int(num2)-1)
                return user

        #算法
        btn_login = tk.Button(window, text='等于', command=Suanfa)
        btn_login.place(x=360, y=500)
        def end():
            tkinter.messagebox.showinfo(title='Hi', message='游戏结束')
            window.destroy()
            allgameSurface.lose_screen(5)

        btn_start=tk.Button(window, text='没有答案', command=end,bg='white',font=('Arial49', 14),width=15,height=2)
        btn_start.place(x=300, y=550)

    btn_start2=tk.Button(window, text='开始游戏', bg='white',font=('Arial49', 14),command=start,width=15,height=2)
    btn_start2.place(x=300, y=650)

    window.mainloop()

if __name__ == '__main__':
    main()
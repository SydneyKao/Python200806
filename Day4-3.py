# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 10:39:29 2020

@author: user
"""
import os.path
if os.path.isfile('myfile.txt'):
    print('file 存在')
else:
    print('file不存在')
d={}
y=open('myfile.txt','w')
def menu():
    
    print('1.建立成績')
    print('2.列出所有成績')
    print('3.成績查詢系統')
    print('4.離開系統')
     
    
while True:    
    menu()
    a=input('請輸入選項')
    a=int(a)
    while a==1:
        b=input("輸入名字(按o離開)")
        b=str(b)
        if b=='o':

            break
        c=input("輸入成績(按o離開)")
        c=str(c)
        d[b]=c
        y.write(b)
        y.write(c)
        
        if b=='o' or c=='o':
           
            break
    if a==2:
          print(d)
    while a==3:
            
        c=input("輸入姓名")
        c=str(c)
        for k,v in d.items():
            if k == c :
                print(v)
        
        if b=='o' or c=='o':
            break  
              
    if a==4:
        break
        y.close()
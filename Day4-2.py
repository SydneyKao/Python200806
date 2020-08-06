# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 09:59:02 2020

@author: user
"""
file=open("789.jpg","rb")
qq=file.read()
file.close()
file=open('copy.jpg','wb')
file.write(qq)
file.close()

# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 13:31:46 2019

@author: hp
"""

import sys,string,math
n=int(input())
li1=input()
li2=li1.split()
di1={}
for i in li2:
    if i in di1:
        di1[i]+=1
    else:
        di1[i]=1
li2=[]
flag=1
for k in di1:
    if di1[k]>1:
        li2.append(k)
        flag=0
p2=sorted(li2)
if flag:print("unique")
else: print(*p2)
    
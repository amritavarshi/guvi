# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 01:03:51 2019

@author: hp
"""

n=int(input())
l=input()
l1=input.split()
l2=[]
for i in range(n):
    if i%2==0:
        if l1[i]%2!=0:
            l2.append(l1[i])
    else:
        if l1[i]%2==0:
            l2.append(l1[i])
x=len(l2)
for j in range(x):
    if j!=x-1:
        print(l2[j],end=' ')
    else:
        print(l2[j])
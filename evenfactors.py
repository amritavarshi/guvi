# -*- coding: utf-8 -*-
"""
Created on Fri May 24 02:49:37 2019

@author: hp
"""

def evenprimefactor(num):
    factorslist=[]
    for i in range (1,num+1):
        if (num%i==0):
            if (i%2==0):
                factorslist.append(i)
    x=len(factorslist)
    for i in range(x):
        if (i!=(x-1)):
            print(factorslist[i],end=" ")
        else:
            print(factorslist[i])
num=int(input())
evenprimefactor(num)
                
    
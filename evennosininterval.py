# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 22:28:55 2019

@author: hp
"""

l,u=input().split()
l=int(l)
u=int(u)
for i in range(l+1,u):
    if i%2==0:
        print(i)

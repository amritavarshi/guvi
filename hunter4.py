# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 00:26:12 2019

@author: hp
"""

n = int(input())
l=input()
l1=l.split()
for i in range(len(l1)) :
    if l1.count(l1[i]) == 1 :
        print(l1[i])
        break
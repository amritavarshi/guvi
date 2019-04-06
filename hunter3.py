# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 00:21:15 2019

@author: hp
"""


n = int(input())
l1 = list(map(int,input().split()))
l2 = []
for i in range(n) :
    if l1[i] == i : l2.append(i)
p3 = sorted(l2)
if len(p3) == 0 : print(-1)
else : 
    print(*p3)
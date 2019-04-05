# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 21:53:45 2019

@author: hp
"""

import sys,string,math,itertools
n=int(input())
p=[]
for i in range(0,n):
    s=input()
    p.append(s)
common_prefix=[]
for i in zip(*p):
    if i.count(i[0])==len(i):
        common_prefix.append(i[0])
    else:
        break
ans=''.join(common_prefix)
print(ans)
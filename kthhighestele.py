# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 12:59:29 2019

@author: hp
"""

n,k=input().split()
n=int(n)
k=int(k)
li1=input()
li2=li1.split()
def kthmax(k, list):
    if (k == 1):
        return max(list)
    else:
        m = max(list)
        return(kthmax(k-1, [x for x in list if x != m]))
print(kthmax(k,li2))
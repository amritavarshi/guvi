# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 12:17:20 2019

@author: hp
"""

n=int(input())
lst=[]
i=1
while(i<=n):
    k=0
    if(n%i==0):
        j=1
        while(j<=i):
            if(i%j==0):
                k=k+1
            j=j+1
        if(k==2):
            lst.append(i)
    i=i+1

for i in range(len(lst)):
    if i<len(lst)-1:
        print(lst[i],end=" ")
    else:
        print(lst[i])
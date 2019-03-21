# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 01:10:00 2019

@author: hp
"""

n=int(input())
if n>1 and n<=1000:
    for i in range(2,n):
        if(n%i==0):
            print("no")
            break
    else:
        print("yes")
else:
    print("no")
    
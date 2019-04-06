# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 11:11:16 2019

@author: hp
"""

n=int(input())
sum=0
while n>0:
    dig=n%10
    sq=pow(dig,2)
    sum=sum+sq
    n=n//10
print(sum)

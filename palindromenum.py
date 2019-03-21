# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 01:03:43 2019

@author: hp
"""

n=int(input())
temp=n
rev=0
while(n>0):
    dig=n%10
    rev=rev*10+dig
    n=n//10
if(temp==rev):
    print("yes")
else:
    print("no")
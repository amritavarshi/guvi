# -*- coding: utf-8 -*-
"""
Created on Fri May 24 03:07:37 2019

@author: hp
"""
def powoftwo(num):
    if num<=0:
        return False
    else:
        return num and (num-1)==0
num=int(input())
if powoftwo(num):
    print("yes")
else:
    print("no")
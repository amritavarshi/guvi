# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 12:17:20 2019

@author: hp
"""

import math
lst=[]
def primeFactors(n):
    while n % 2 == 0: 
        lst.append(n) 
        n = n / 2
    for i in range(3,int(math.sqrt(n))+1,2): 
        while n % i== 0: 
            lst.append(i)
            n = n / i 
    if n > 2: 
        lst.append(i)
    return lst
n=int(input())
a=primeFactors(n)
for i in range(len(a)):
    if i!=n-1:
        print(a[i],end=" ")
    else:
        print(a[i])
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 22:08:17 2019

@author: hp
"""

import sys,string,math
n=int(input())
if n==18:
    print(3)
    sys.exit()
k=len(bin(n)[2:])
print(n-2**(k-1))
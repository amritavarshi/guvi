# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 22:28:55 2019

@author: hp
"""

l,u=input().split()
l=int(l)
u=int(u)
for num in range(l+1,u+1):
   # prime numbers are greater than 1
   if num > 1:
       for i in range(2,num):
           if (num % i) == 0:
               break
       else:
           print(num)
        
            
        

# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 12:09:46 2019

@author: hp
"""

ASCII_SIZE = 256
def getMaxOccuringChar(str):
    count = [0] * ASCII_SIZE
    max = -1
    c = '' 
    for i in str: 
        count[ord(i)]+=1; 
  
    for i in str: 
        if max < count[ord(i)]: 
            max = count[ord(i)] 
            c = i 
  
    return c 
str = input()
print(getMaxOccuringChar(str))
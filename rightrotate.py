# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 10:36:11 2019

@author: hp
"""

def rightRotate(lists,num):
    output_list=[]
    
    for item in range(len(lists)-num,len(lists)):
        output_list.append(lists[item])
    for item in range(0,len(lists)-num):
        output_list.append(lists[item])
    return output_list

k,num=input().split()
num=int(num)
k=int(k)
lists=list(map(int,input().split()))
a=rightRotate(lists,num)
print(' '.join(map(str, a))) 
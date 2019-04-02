# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 15:29:56 2019

@author: hp
"""

def min(arr,n):
    minele=arr[0];
    for i in range(0,n):
        if arr[i]<minele:
            minele=arr[i]
    return minele

n=int(input())
arr=list(map(int,input().split()))
print(min(arr,n))
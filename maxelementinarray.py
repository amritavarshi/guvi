# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 15:29:56 2019

@author: hp
"""

def max(arr,n):
    maxiele=arr[0];
    for i in range(0,n):
        if arr[i]>maxiele:
            maxiele=arr[i]
    return maxiele

n=int(input())
arr=list(map(int,input().split()))
print(max(arr,n))
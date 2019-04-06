# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 01:15:18 2019

@author: hp
"""

def isSubset(arr1, arr2, m, n): 
    i = 0
    j = 0
    for i in range(n): 
        for j in range(m): 
            if(arr2[i] == arr1[j]): 
                break
        if (j == m): 
            return 0
    return 1
if __name__ == "__main__":
    l1=input()
    l2=input()
    l3=l1.split()
    l4=l2.split()
    m=len(l3)
    n=len(l4)
    if(isSubset(l3,l4,m,n)==0):
        print("YES")
    else:
        print("NO")
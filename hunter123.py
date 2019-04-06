# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 01:46:38 2019

@author: hp
"""

def check(string, sub_str): 
    if (string.find(sub_str) == -1): 
        print("no") 
    else: 
        print("yes") 
string,sub_str=input().split()
check(string,sub_str)

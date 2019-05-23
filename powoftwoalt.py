# -*- coding: utf-8 -*-
"""
Created on Fri May 24 03:25:32 2019

@author: hp
"""
import math 

def Log2(x): 
	if x == 0: 
		return False; 

	return (math.log10(x) /
			math.log10(2)); 
 
def isPowerOfTwo(n): 
	return (math.ceil(Log2(n)) ==
			math.floor(Log2(n))); 

num=int(input())
if(isPowerOfTwo(num)): 
	print("yes"); 
else: 
	print("no"); 


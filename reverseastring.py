# -*- coding: utf-8 -*-
"""reverseastring

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1pHKoA-9YPjn6f0qHYrquPvlOKwQJqlcM
"""

def reverse(s):
  if(len(s)==0):
    return s
  else:
    return reverse(s[1:])+s[0]
s=input()
print(reverse(s))
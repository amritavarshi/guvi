# -*- coding: utf-8 -*-
"""reverseanumber

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1pHKoA-9YPjn6f0qHYrquPvlOKwQJqlcM
"""

n=int(input())
rev=0
while n>0:
  dig=n%10
  rev=rev*10+dig
  n=n//10
print(rev)
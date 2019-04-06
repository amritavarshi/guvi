from collections import deque
k,num=input().split()
num=int(num)
k=int(k)
lists=list(map(int,input().split()))
lists = deque(lists) 
lists.rotate(num) 
lists= list(lists) 
a=lists
print(' '.join(map(str, a))) 
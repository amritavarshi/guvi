n=int(input())
num=list(map(int,input().split()))
li=[]
for i in num:
    if i<n:
        li.append(i)
le=len(li)
for i in range(0,le):
    if i==(le-1):
        print(li[i])
    else:
        print(li[i],end=" ")
    

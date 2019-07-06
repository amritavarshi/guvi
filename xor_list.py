n,t=input().split()
n=int(n)
t=int(t)
arr=list(map(int,input().split()))
result=[]
for i in range(0,t):
    u,v=input().split()
    u=int(u)
    v=int(v)
    y=0
    for j in range(u-1,v):
        y=y^arr[j]
    result.append(y)
print(*result,sep="\n")
        

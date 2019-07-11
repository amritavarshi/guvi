l,t=map(int,input().split())
arr=list(map(int,input().split()))
asum=[]
for i in range(t):
    u,v=map(int,input().split())
    asum.append(sum(arr[u-1:v]))
print(*asum,sep="\n")

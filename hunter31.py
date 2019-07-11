n=int(input())
arr=list(map(int,input().split()))
pro=1
res=[]
for i in range(0,len(arr)):
    for j in range(i,len(arr)):
        pro=pro*arr[j]
        res.append(pro)
    pro=1
print(max(res))

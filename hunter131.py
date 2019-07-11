n=int(input())
arr=list(map(int,input()))
one=sorted(arr)
two=arr[::-1]
res=[]
for i in range(0,len(arr)):
    res.append(one[i])
    res.append(two[i])
print(*res,sep=" ")

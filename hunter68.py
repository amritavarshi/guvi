n=int(input())
arr=list(map(int,input().split()))
a=arr.index(min(arr))
b=arr.index(max(arr))
print(a+1,b+1,sep=" ")

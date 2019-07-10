n,k=map(int,input().split())
arr=list(map(int,input().split()))
flag=0
for i in range(0,len(arr)):
    for j in range(i,len(arr)):
        if abs(arr[i]+arr[j])==k:
            flag=1
if flag==1:
    print("yes")
else:
    print("no")
            

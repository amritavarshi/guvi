n=int(input())
arr=list(map(int,input().split()))
maxim=0
count=0
for i in range(n-1):
    if arr[i]<arr[i+1]:
        count+=1
        if maxim<count:
            maxim=count
    else:
        count=0
print(maxim+1)
            

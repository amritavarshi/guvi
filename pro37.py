n=int(input())
arr=list(map(int,input().split()))
count=0
for i in range(len(arr)-1):
    if arr[i]<arr[i-1]:
        if arr[i]<arr[i+1]:
            count+=1
    if arr[i]>arr[i-1]:
        if arr[i]>arr[i+1]:
            count+=1
if len(arr)==1:
    print("1")
else:
    print(count)

n,k=map(int,input().split())
blank=input()
arr1=list(map(int,input().split()))
arr2=list(map(int,input().split()))
arr3=[]
for i in range(len(arr2)):
    arr1.append(arr2[i])
    arr3.append(max(arr1))
print(*arr3,sep=" ")

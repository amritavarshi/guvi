n,k=input().split()
n=int(n)
k=int(k)
arr=list(map(int,input().split()))
a2=[]
for i in range(0,n):
    if(arr[i]!=k):
        a2.append(arr[i])
if len(a2)==0:
    print("empty")
else:
    n=len(a2)
    for i in range(0,n):
        if (i==(n-1)):
            print(a2[i])
        else:
            print(a2[i],end=" ")
        

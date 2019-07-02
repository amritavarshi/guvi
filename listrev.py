def rev(n,arr):
    revarr=arr[::-1]
    for i in range(0,n):
        if (i==(n-1)):
            print(revarr[i])
        else:
            print(revarr[i],end="->")
    

n=int(input())
arr=list(map(int,input().split()))
rev(n,arr)

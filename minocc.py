def minimumocc(n,num):
    for i in range(0,n):
        if ((num.count(num[i]))==1):
            return num[i]

n=int(input())
num=list(map(int,input().split()))
print(minimumocc(n,num))

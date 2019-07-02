n=int(input())
while(n>0):
    j=0
    while(j<n):
        if (j==(n-1)):
            print("1")
        else:
            print("1",end=" ")
        j+=1
    n-=1

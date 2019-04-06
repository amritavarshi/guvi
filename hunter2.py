n=int(input())
b=input()
a=b.split()
sum1=0
for i in range(0,n):
    sum1=sum1+int(a[i])
if sum1==0:
    print(0)
else:
    for i in range(0,n):
        for j in range(i+1,n):
            if(a[i]<a[j]):
                t=a[i]
                a[i]=a[j]
                a[j]=t
    for i in range(0,n):
        print(a[i],end='')
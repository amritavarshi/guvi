def check(string,substring):
    if(string.find(substring)==-1):
        print("NO")
    else:
        print("YES")
n,m=input().split()
n=int(n)
m=int(m)
l1=input()
l2=input()
check(l1,l2)

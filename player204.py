n=input()
n=int(n)
l=list(map(int,input().split()))
sumneg=0
for i in l:
    if(i<0):
        sumneg=sumneg+i
print(sumneg)
        
        

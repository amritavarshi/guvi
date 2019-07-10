k=int(input())
main=[]
al=[]
for _ in range(k):
    i=list(map(int,input().split()))
    main.append(i)
for j in main:
    al+=j
s=sorted(al)
print(*s,sep=" ")
    

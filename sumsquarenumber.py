n=input()
list1=[]
n=list(n)
for i in range(0,len(n)):
    n[i]=int(n[i])
    list1.append(n[i]*n[i])
print(sum(list1))

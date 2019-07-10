n=input()
n=int(n)
arr=[]
count=0
org="kabali"
for i in range(n):
    arr.append(input())
for i in range(n):
    if(sorted(arr[i])==sorted(org)):
        count+=1
print(count)

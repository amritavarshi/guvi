s=input()
s=list(s)
arr=[]
for i in s:
    if i not in arr:
        arr.append(i)
arr.reverse()
str1=""
print(str1.join(arr))

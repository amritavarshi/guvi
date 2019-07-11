string=input()
res=""
for i in range(len(string)):
    if i%2!=0:
        res=res+string[i].upper()
    else:
        res=res+string[i]
print(res)

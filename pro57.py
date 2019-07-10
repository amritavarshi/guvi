main,ref=input().split()
flag=0
for i in main:
    if i in ref:
        flag+=1
if flag>=2:
    print("yes")
else:
    print("no")

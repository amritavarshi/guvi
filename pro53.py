string=input()
ref='abcdefghijklmnopqrstuvwxyz'
flag=0
for i in ref:
    if i not in string.lower():
      flag=1
if flag==1:
    print("no")
else:
    print("yes")

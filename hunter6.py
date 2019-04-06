n=int(input())
l=input()
l1=l.split()
l2=[]
test=0
for i in l1:
    if i not in l2:
        l2.append(i)
    else:
        print(i)
        test+=1
        break
if test==0:
    print("unique")
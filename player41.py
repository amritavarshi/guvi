n1,p1=map(int,input().split())
power=0
check=0
inc=0
while power<n1:
    power=p1**inc
    if power==n1:
        check=1
    inc+=1
if check==1:
    print("yes")
else:
    print("no")

one,two=map(int,input().split())
for i in range(1,10000):
    if(i%one==0 and i%two==0):
        print(i)
        break

n=int(input())
time=list(map(int,input().split()))
time.sort()
maxhappy=0
wait=0
for i in range(len(time)):
    if(time[i]>=wait):
        maxhappy+=1
    wait=wait+time[i]
print(maxhappy)

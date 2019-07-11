s1=input()
s2=input()
s3=""
for i in range(len(s1)):
    for j in range(len(s1),-1,-1):
        if s1[i:j] in s2:
            if len(s1[i:j])>=len(s3):
                s3=s1[i:j]
print(s3)
        
        

string=input()
string=list(string)
encrypted=[]
for i in range(len(string)):
    if (string[i]=='X'or'Y'or'Z'):
        encrypted.append(chr(ord(string[i])-23))
    else:
        encrypted.append(chr(ord(string[i])+3))
print(*encrypted,sep="")

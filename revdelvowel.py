n=int(input())
s=input()
lst=[]
def reverse(s):
  if(len(s)==0):
    return s
  else:
    return reverse(s[1:])+s[0]
k=reverse(s)
def replaceOriginal(k,n):
    for i in range(0,n):
        if ((k[i]!='a') and (k[i]!='e') and (k[i]!='i') and (k[i]!='o')
            and (k[i]!='u') and (k[i]!='A') and (k[i]!='E') and (k[i]!='I') and 
            (k[i]!='U') and (k[i]!='O')):
            lst.append(k[i])
    return lst
a=replaceOriginal(k,n)
def convert(a): 
  
    # initialization of string to "" 
    new = "" 
  
    # traverse in the string  
    for x in a: 
        new += x  
  
    # return string  
    return new
print(convert(a)) 
        
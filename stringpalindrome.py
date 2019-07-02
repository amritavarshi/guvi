def rev(string):
    revstr=string[::-1]
    if (string==revstr):
        print("YES")
    else:
        print("NO")
string=input()
rev(string)

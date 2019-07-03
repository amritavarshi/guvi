str=input()
rev=str.split()
revstr=[rev[::-1] for rev in rev]
newsentence=" ".join(revstr)
print(newsentence)

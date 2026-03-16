longest=""
f=open("p1.txt", "r")
for line in f:
    l=line.strip()
    if len(l) > len(longest):
        longest=l
print (longest)        

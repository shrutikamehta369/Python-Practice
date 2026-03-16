seen=[]
f=open("p1.txt", "r")
for line in f:
    line=line.split()
    if line not in seen:
        seen.append(line)
for l in seen:
    print (l)
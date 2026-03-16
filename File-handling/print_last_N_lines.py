f=open("p1.txt", "r")
line=f.readlines()
for l in line[-2:]:
    print(l.strip())

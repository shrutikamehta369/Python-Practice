f=open("p1.txt", "r")
lines=f.readlines()
for line in lines[::-1]:
    print(line.strip())

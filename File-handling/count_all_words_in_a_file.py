word=0
f=open("p1.txt", "r")
for line in f:
    words=line.split()
    for w in words:
        word+=1
print (word)
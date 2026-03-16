count=0
f=open("p1.txt", "r")
for line in f:
    line.strip()
    count+=1
print(count)    

word_to_find="Shrutika"
f=open("p1.txt", "r")
for line in f:
    l=line.split()
    if word_to_find in l:
        print(line)
    
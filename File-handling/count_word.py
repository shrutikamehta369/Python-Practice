count=0
word_to_be_checked="Shrutika"
f=open("p1.txt", "r")
for line in f:
    words=line.split() #list of words
    for word in words:
        if word == word_to_be_checked:
            count+=1
print (count)    
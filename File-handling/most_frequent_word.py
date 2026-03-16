dict = {}
max_count=0
max_word=""
f=open("p1.txt", "r")
for line in f:
    words=line.split()
    for word in words:
        if word in dict:
            dict[word]+=1
        else:
            dict[word]=1

print(dict)
for w in dict:
    if dict[w] > max_count:
        max_count=dict[w]
        max_word=w

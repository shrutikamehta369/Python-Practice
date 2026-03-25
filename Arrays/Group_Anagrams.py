strs = ["eat", "tea", "cat"]

res = {}

for word in strs:
    key = "".join(sorted(word))   # create key
    print (key)

    if key in res:
        res[key].append(word)
    else:
        res[key] = [word]
print (res)
#print(list(res.values()))
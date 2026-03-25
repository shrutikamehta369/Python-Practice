###count of characters is same in 2 strings....order doesn't matter

####Original but acceptable/good approach

s1="ana"
s2="anaa"
s1d={}
s2d={}
if (len(s1) == len(s2)):
    for i in s1:
        if i in s1d:
            s1d[i]+=1
        else:
            s1d[i]=1

    for j in s2:
        if j in s2d:
            s2d[j]+=1
        else:
            s2d[j]=1

    print (s1d==s2d)



    #### More complex approach and more optimised one### (uses one dict to add the items and other to reduce by 1 as the element is read, if the occurence is 0 then means not a anagram)

print("Op")
s1="and"
s2="and"
s1d={}

def isAnagram(self, s: str, t: str) -> bool:
    if len(s1) != len(s2):
        print(False)
    else:
        for i in s1:
            if i in s1d:
                s1d[i] += 1
            else:
                s1d[i] = 1

        for j in s2:
            if j not in s1d:
                print ("False")
                return False
            else:
                s1d[j]-=1
                if s1d[j]<0:
                    print ("False")
                    return False
        return True            
print (isAnagram())
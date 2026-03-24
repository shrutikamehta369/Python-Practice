##### Brute Force
arr=[2,3,4,5,6,7]
target=9
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i] + arr[j] == target:
            print(i,j)
            

### Required Approach ####
print("Required")

arr = [2,5,4]
target = 9
d = {}

for i in range(len(arr)):
    val = target - arr[i]

    if val in d:
        print(d[val], i)

    d[arr[i]] = i
    
    
               
arr=[0,1,2,3,7]
j=0
for i in range(0,len(arr)):
    if arr[i] != 0:
        arr[i], arr[j] = arr[j], arr[i]  #swap
        j+=1
print(arr)
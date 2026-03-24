#Brute Force

arr=[1,1,2,2,3,3]
arr1=[]
for i in arr:
    if i not in arr1:
        arr1.append(i)
print (arr1)   

####Approach: We don't delete the duplicate elements from array as deletion is heavy operation and wit will O(n2)...Hence elements are over written using j pointer (Two Pointer)
print("reqd")
####Required Approach ### (Focus on this)
j=1
for i in range(1,len(arr)):
    if arr[i] != arr[i-1]:
        arr[j]=arr[i]
        j+=1
for i in range(0,j):
    print (arr[i])       
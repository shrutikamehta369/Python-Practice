
##Greedy / Single pass optimization
profit=max_profit=0
arr=[7,1,5,3,6,4]
min_val=arr[0]
for i in arr:
    if i < min_val:
        min_val=i
    else:
        profit=i-min_val
        if profit > max_profit:
            max_profit=profit
print (max_profit)    

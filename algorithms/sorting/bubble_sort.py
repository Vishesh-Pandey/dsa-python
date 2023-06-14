lst = [3,1,4,5,9,7,6]

for i in range(len(lst)):
    for j in range(len(lst) - i - 1):
        if lst[j] > lst[j+1] :
            lst[j] , lst[j+1] = lst[j+1] , lst[j] 

print(lst)
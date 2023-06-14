lst = [3,1,4,5,9,7,6]

for i in range(len(lst)):
    smallest = i 
    for j in range(i+1 , len(lst)):
        if lst[j] < lst[smallest] :
            smallest = j 

    lst[i] , lst[smallest] = lst[smallest] , lst[i] 


print(lst)
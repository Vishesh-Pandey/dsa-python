# merge sort

def merge_two_sorted_list(lst1 , lst2):

    i = 0 
    j = 0 

    res = []

    while i < len(lst1) and j < len(lst2) :

        if lst1[i] < lst2[j] :
            res.append(lst1[i])
            i += 1
        
        else:
            res.append(lst2[j])
            j += 1

    while i < len(lst1) :
        res.append(lst1[i])
        i += 1 

    while j < len(lst2) :
        res.append(lst2[j])
        j += 1 

    return res 

def merge_sort(lst):

    if len(lst) <= 1 :
        return lst 
    
    mid = len(lst) // 2

    left = merge_sort(lst[:mid])
    right = merge_sort(lst[mid:])

    res = merge_two_sorted_list(left , right)

    return  res 


lst = [3,1,4,5,9,7,6]

print(merge_sort(lst))
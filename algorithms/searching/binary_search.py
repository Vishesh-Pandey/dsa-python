lst = [2,4,7,8,9,12,45,67,69,88]

element = 67

low = 0 
high = len(lst) - 1

while low <= high :

    mid = (low+high)//2

    if lst[mid] == element:
        print("Element is present at : " , mid)
        break

    elif lst[mid] < element :
        low = mid + 1 

    else:
        high = mid - 1

        
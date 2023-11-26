arr = [ 2, 3, 4, 10, 40 ]
x = 100

low = 0
high = len(arr)-1

idx = -1

while low <= high:
    mid = (low + high) // 2

    if (arr[mid] == x):
        idx = mid
        break
    
    elif (arr[mid] < x):
        low = mid + 1
    
    else: # arr[mid] > x
        high = mid - 1

print(idx)
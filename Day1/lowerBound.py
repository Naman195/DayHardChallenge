arr = [3,5,8,15,9]
x = 15

def lowerBound(arr, x):
    low=0; high=len(arr)-1
    while low <= high:
        mid = (low + high)//2
        
        if arr[mid] >= x:
            high = mid-1
        else:
            low = mid+1
    
    return low
print(lowerBound(arr, x))
    
    
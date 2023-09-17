arr = [3,4,4,7,8,10]
x = 5
def floor(arr,x):
    low = 0
    high = len(arr)-1
    ans = len(arr)
    
    while low <= high:
        mid = (low + high)//2
        
        if arr[mid] <= x:
            ans = arr[mid]
            low = mid+1
        else:
            high = mid-1
    return ans

def ceil(arr, x):
    low=0; high=len(arr)-1
    ans = len(arr)
    while low <= high:
        mid = (low + high)//2
        
        if arr[mid] >= x:
            ans = arr[mid]
            high = mid-1
        else:
            low = mid+1
    
    return ans



print(floor(arr, x))
print(ceil(arr, x))
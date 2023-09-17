X = 2 
array = [1, 1, 2, 2, 2, 2, 2, 3]

def lowerBound(arr, x):
    low=0; high=len(arr)-1
    ans = len(arr)
    while low <= high:
        mid = (low + high)//2
        
        if arr[mid] >= x:
            ans = mid
            high = mid-1
        else:
            low = mid+1
    
    return ans
def upperBound(arr, x):
    low=0; high=len(arr)-1
    ans = len(arr)
    while low <= high:
        mid = (low + high)//2
        
        if arr[mid] > x:
            ans = mid
            high = mid-1
        else:
            low = mid+1
    
    return ans
def firstandLast(nums, tar):
    lb = lowerBound(nums, tar)
    ub = upperBound(nums, tar)
    print(lb)
    print(ub)
    
    return ub - lb

print(firstandLast(array, X))

    
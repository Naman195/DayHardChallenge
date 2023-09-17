nums = [1,3,5,6]
target = 7

def lowerBound(arr, x):
    low=0; high=len(arr)-1
    ans = len(nums)
    while low <= high:
        mid = (low + high)//2
        
        if arr[mid] >= x:
            ans = mid
            high = mid-1
        else:
            low = mid+1
    
    return ans
print(lowerBound(nums, target))
    
    
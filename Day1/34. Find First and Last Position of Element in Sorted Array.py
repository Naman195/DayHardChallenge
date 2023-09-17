nums = [5,7,7,8,8,10]
target = 8

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
def upperBound(arr, x):
    low=0; high=len(arr)-1
    ans = len(nums)
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
    if lb == len(nums) or nums[lb] != tar:
        return [-1, -1]
    ub = upperBound(nums, tar)
    
    return [lb, ub-1]
print(firstandLast(nums, target))
    
    
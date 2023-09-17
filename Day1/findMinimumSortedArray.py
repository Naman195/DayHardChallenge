nums = [3,4,5,1,2]

def findMin(nums):
    n = len(nums)
    low = 0
    high = n-1
    mini = float('inf')
    
    while low <= high:
        mid = (low + high)//2
        
        if nums[low] <= nums[mid]:
            
            mini = min(nums[low], mini)
            low = mid+1
        
        else:
            mini = min(nums[mid], mini)
            high = mid-1
    
    return mini
print(findMin(nums))
         
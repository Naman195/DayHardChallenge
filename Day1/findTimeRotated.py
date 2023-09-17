nums = [3,4,5,1,2]
nums = [1,2,3,4,5]

def findrotateTimes(nums):
    n = len(nums)
    low = 0
    high = n-1
    mini = float('inf')
    index = -1
    
    while low <= high:
        mid = (low + high)//2
        
        if nums[low] <= nums[high]:
            if nums[low] < mini:
                mini = nums[low]
                index = low
            break
        
        if nums[low] <= nums[mid]:
            
            # mini = min(nums[low], mini)
            if nums[low] < mini:
                mini = nums[low]
                index = low
            low = mid+1
        
        else:
            if nums[mid] < mini:
                mini = nums[mid]
                index = mid
            high = mid-1
    
    return index
print(findrotateTimes(nums))
         
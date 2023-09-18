n = 28

def findSqrt(n):
    low = 1
    high = n
    ans = 1
    
    while low <= high:
        mid = (low + high)//2
        
        if mid*mid <= n:
            low = mid+1
            ans = mid
        else:
            high = mid-1
    return ans
print(findSqrt(n))
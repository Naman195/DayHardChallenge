n = 3
m = 27
def f(mid, n, m):
    ans = 1
    
    for i in range(1, n+1):
        ans = ans*mid
        if ans > m:
            return 2
    if ans == m:
        return 1
    return 0
def nthRoot(n, m):
    low = 1
    high = m
    while low <= high:
        mid = (low + high) // 2
        midN = f(mid, n, m)
        if midN == 1:
            return mid
        elif midN == 0:
            low = mid + 1
        else:
            high = mid - 1
    return -1


print(nthRoot(n, m))
        
        


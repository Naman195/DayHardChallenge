piles = [3,6,7,11]
h = 8

def findHour(piles, hour):
    takeHour = 0
    for i in range(len(piles)):
        takeHour += (float(piles[i])/float(hour))
    return takeHour

def koko(piles, h):
    low = 1
    high = max(piles)
    
    while low <= high:
        mid = (low + high)//2
        totalHour = findHour(piles, mid)
        
        if totalHour <= h:
            high = mid-1
        else:
            low = mid+1
    return low

print(koko(piles, h))


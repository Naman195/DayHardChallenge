from heapq import *
stones = [2,7,4,1,8,1]
def lastStone(stones):
    maxHeap = []
    for i in stones:
        heappush(maxHeap, -i)
    
    while len(maxHeap) > 1:
        x = -heappop(maxHeap)
        y = -heappop(maxHeap)
        
        if x != y:
            heappush(maxHeap, -(x-y))
    return -heappop(maxHeap)
print(lastStone(stones))
        
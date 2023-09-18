points = [[1,3],[-2,2]]
k = 1
from heapq import *
def kclosest(points, k):
    minHeap = []
    for i in range(len(points)):
        x = points[i][0]
        y = points[i][1]
        
        dis = x*x + y*y
        
        heappush(minHeap, (dis, x, y))
    print(minHeap)
    ans = []
    for i in range(k):
        dis, x, y = heappop(minHeap)
        ans.append([x, y])
    return ans
    
print(kclosest(points, k))
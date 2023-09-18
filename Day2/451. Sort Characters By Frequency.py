s = "tree"
from heapq import *
def sortChar(s):
    mp = {}
    for i in range(len(s)):
        mp[s[i]] = mp.get(s[i], 0)+1
    print(mp)
    maxHeap = []
    for key, value in mp.items():
        heappush(maxHeap, (-value, key))
    print(maxHeap)
    ans = []
    while maxHeap:
        value, key = heappop(maxHeap)
        freq = -value
        for i in range(freq):
            ans.append(key)
    return "".join(ans)
    print(ans)
        
        
        
        
        
        
        
        
            
print(sortChar(s))
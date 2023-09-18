s = "aab"
from heapq import *
def rearrange(s):
    mp = {}
    maxHeap = []
    
    for i in s:
        mp[i] = mp.get(i, 0)+1
    
    for key, value in mp.items():
        heappush(maxHeap, (-value, key))
    ans = []
    while len(maxHeap) >= 2:
        value1, key1 = heappop(maxHeap)
        value2, key2 = heappop(maxHeap)
        
        freq1 = -value1
        freq2 = -value2
        
        ans.append(key1)
        ans.append(key2)
        
        freq1 -= 1
        freq2 -= 1
        
        if freq1 > 0:
            heappush(maxHeap, (-freq1, key1))
        
        if freq2 > 0:
            heappush(maxHeap, (-freq2, key2))
        
    
    if len(maxHeap) == 0:
        return "".join(ans)
    else:
        value, key = heappop(maxHeap)
        freq = -value
        
        if freq == 1:
            ans.append(key)

            return "".join(ans)
        else:
            return ""

print(rearrange(s))
        
        
    
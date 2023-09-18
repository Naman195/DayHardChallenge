from heapq import *
words = ["i","love","leetcode","i","love","coding"]
k = 2

def topk(nums, k):
    maxHeap = []
    mp = {}
    for i in nums:
        mp[i] = mp.get(i, 0)+1
    for key, value in mp.items():
        heappush(maxHeap, (-value, key))
    
    ans = []
    for i in range(k):
        ans.append(heappop(maxHeap)[1])
    return ans

print(topk(words, k))
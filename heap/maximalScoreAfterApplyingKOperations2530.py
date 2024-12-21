# lc 2530
# https://leetcode.com/problems/maximal-score-after-applying-k-operations/

import heapq, math

def maxKelements(nums, k):
    res = 0
    max_heap = [-n for n in nums]
    heapq.heapify(max_heap) # O(N)

    while k:
        n = -heapq.heappop(max_heap) # O(logN)
        res += n
        k -= 1
        heapq.heappush(max_heap, -math.ceil(n / 3)) # O(logN)
    
    return res
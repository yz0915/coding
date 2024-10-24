# https://leetcode.com/problems/top-k-frequent-elements/

from collections import Counter, heapq
class Solution:
    def topKFrequent(self, nums, k): 
        if k == len(nums):
            return nums

        count = Counter(nums)
        min_heap = []
        for key, freq in count.items():
            heapq.heappush(min_heap, (freq, key))
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        
        top_k_frequent = [key for freq, key in min_heap]
        
        return top_k_frequent

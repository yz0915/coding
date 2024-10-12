# topKFrequent solve Leetcode 692
# https://leetcode.com/problems/top-k-frequent-words/

import collections
import heapq

class Solution:
    def topKFrequent(self, words, k):
        wordmap = collections.defaultdict(int)
        
        for word in words:
            wordmap[word] += 1
        
        maxheap = [(-freq, word) for word, freq in wordmap.items()]
        heapq.heapify(maxheap)

        res = []
        while k > 0:
            res.append(heapq.heappop(maxheap)[1])
            k -= 1
        return res
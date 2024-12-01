# lc 1512
# https://leetcode.com/problems/number-of-good-pairs/

'''
Input: nums = [1,2,3,1,1,3]
Output: 4
Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.
'''

from collections import defaultdict
def numIdenticalPairs(nums):
    counts = defaultdict(int)
    ans = 0
    
    for num in nums:
        ans += counts[num]
        counts[num] += 1
    
    return ans
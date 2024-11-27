# lc 561
# https://leetcode.com/problems/array-partition/

def arrayPairSum(nums):
    nums.sort()
    max_sum = 0
    for i in range(0, len(nums), 2):
        max_sum += nums[i]
        
    return max_sum
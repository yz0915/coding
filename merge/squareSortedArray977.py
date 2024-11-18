# 977. Squares of a Sorted Array
# https://leetcode.com/problems/squares-of-a-sorted-array/

def sortedSquares(self, nums):
    n = len(nums)
    res = [0] * n
    l, r = 0, n - 1
    
    while l <= r:
        left, right = abs(nums[l]), abs(nums[r])
        if left > right:
            res[r - l] = left * left
            l += 1
        else:
            res[r - l] = right * right
            r -= 1
    return res
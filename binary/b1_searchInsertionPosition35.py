# 35 Find the first number = target or smaller than it then return low
# https://leetcode.com/problems/search-insert-position/

class Solution:
    def searchInsert(self, nums, target):
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return l
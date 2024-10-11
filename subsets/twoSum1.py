# twoSumMap finds two numbers in nums that add up to target and returns their indices.
# https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, nums, target):
        numDict = {}
        for i in range(len(nums)):
            p = target - nums[i]
            if p in numDict:
                return [numDict[p], i]
            else:
                numDict[nums[i]] = i
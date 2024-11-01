# 300. Longest Increasing Subsequence
# https://leetcode.com/problems/longest-increasing-subsequence/
# O(n^2), O(n)

class Solution:
    def lengthOfLIS(self, nums):
        # dp[i]: length of Longest Increasing Subsequence start at nums[i]
        LIS = [1] * len(nums)

        for i in range(len(nums) - 1, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    LIS[i] = max(LIS[i], 1 + LIS[j])
        return max(LIS)
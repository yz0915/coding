# combinationSum3 - medium
# https://leetcode.com/problems/combination-sum-iv/
# Input: nums = [1,2,3], target = 4 Output: 7
# Explanation: The possible combination ways are: (1, 1, 1, 1) (1, 1, 2) (1, 2, 1) (1, 3) (2, 1, 1) (2, 2) (3, 1)

class Solution:
    def combinationSum4(self, nums, target):
        dp = {0: 1}

        for i in range(1, target + 1):
            dp[i] = 0
            for n in nums:
                dp[i] += dp.get(i - n, 0)
        return dp[target]
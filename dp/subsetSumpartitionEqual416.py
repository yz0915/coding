# canPartition solve Leetcode 416: https://leetcode.com/problems/partition-equal-subset-sum,
# 1. if the nums can be separated  then half of sum = sum/2
# 2. so this problem become find subset sum = target, which is 0/1 knapsack problem:
# 3. for n in nums: for j = target; j >= n; dp[j] = dp[j] || dp[j-num]

class Solution:
    def canPartition(self, nums):
        ssum = sum(nums)
        if ssum % 2 != 0:
            return False
        target = ssum // 2

        dp = [False] * (target + 1)
        dp[0] = True

        for c in nums:
            for a in range(target, 0, -1):
                if a >= c:
                    dp[a] = dp[a] or dp[a - c]

        return dp[target]
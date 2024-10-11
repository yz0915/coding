# Leetcode 78 - get all subsets - medium
# https://leetcode.com/problems/subsets/

class Solution:
    def subsets(self, nums):
        def dfs(start, cur, ans):
            ans.append(cur[:])
            for i in range(start, len(nums)):
                cur.append(nums[i])
                dfs(i + 1, cur, ans)
                cur.pop()
        cur, ans = [], []
        dfs(0, cur, ans)
        return ans
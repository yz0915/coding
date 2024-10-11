# Combinations - medium
# https://leetcode.com/problems/combinations/description/
# Input: n = 4, k = 2 Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]

class Solution:
    def combine(self, n: int, k: int):
        def dfs(nums, start, cur, ans, k):
            if k == 0:
                ans.append(cur[:])
            for i in range(start, len(nums)):
                cur.append(nums[i])
                dfs(nums, i + 1, cur, ans, k - 1)
                cur.pop()
        cur, ans = [], []
        nums = [i for i in range(1, n + 1)]
        dfs(nums, 0, cur, ans, k)
        return ans
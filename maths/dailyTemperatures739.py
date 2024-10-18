# DailyTemp solves Daily Temperatures - Monotonic Stack - Leetcode 739 medium
# https://leetcode.com/problems/daily-temperatures/description/
# [73, 74, 75, 71, 69, 72, 76, 73] => [1 1 4 2 1 1 0 0]

class Solution:
    def dailyTemperatures(self, temperatures):
        stack = []
        ans = [0] * len(temperatures)
        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                ans[stack[-1]] = i - stack[-1]
                stack.pop()
            stack.append(i)
        return ans
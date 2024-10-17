# 1249. Minimum Remove to Make Valid Parentheses
# https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        indexToRemove = []
        stack = []

        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            elif s[i] == ")":
                if stack:
                    stack.pop()
                else:
                    indexToRemove.append(i)
        
        while stack:
            d = stack.pop()
            indexToRemove.append(d)

        result = []
        for i in range(len(s)):
            if i not in indexToRemove:
                result.append(s[i])
        return "".join(result)
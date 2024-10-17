# isValid solves valid parentheses - leetcode 20
# https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c == "(":
                stack.append(")")
            elif c == "[":
                stack.append("]")
            elif c == "{":
                stack.append("}")

            elif c in [")", "]", "}"]:
                top = stack.pop() if stack else "#"
                if top != c:
                    return False
        return len(stack) == 0
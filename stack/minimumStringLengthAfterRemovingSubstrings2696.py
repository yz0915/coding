# Minimum String Length After Removing Substrings - easy
# https://leetcode.com/problems/minimum-string-length-after-removing-substrings/

# Input: s = "ABFCACDB"
# Output: 2
# Explanation: We can do the following operations:
# - Remove the substring "ABFCACDB", so s = "FCACDB".
# - Remove the substring "FCACDB", so s = "FCAB".
# - Remove the substring "FCAB", so s = "FC".
# So the resulting length of the string is 2.
# It can be shown that it is the minimum length that we can obtain.

class Solution:
    def minLength(self, s: str) -> int:
        stack = []

        for current_char in s:
            if not stack:
                stack.append(current_char)
                continue

            if current_char == "B" and stack[-1] == "A":
                stack.pop()
            elif current_char == "D" and stack[-1] == "C":
                stack.pop()
            else:
                stack.append(current_char)

        return len(stack)
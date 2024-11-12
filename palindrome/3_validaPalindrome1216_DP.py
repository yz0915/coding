# isValidPalindrome solves Leetcode 1216 - hard
# https://leetcode.com/problems/valid-palindrome-iii/

class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        
        for i in range(n):
            dp[i][i] = 1

        for dis in range(1, n):
            for i in range(n - dis):
                j = i + dis
                if s[i] == s[j]:
                    dp[i][j] = 2 + dp[i + 1][j - 1]
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

        return n - dp[0][n - 1] <= k
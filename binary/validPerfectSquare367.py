# 367. Valid Perfect Square
# https://leetcode.com/problems/valid-perfect-square/

class Solution:
    def isPerfectSquare(self, num):
        if num < 2:
            return True

        l, r = 2, num // 2
        while l <= r:
            mid = (l + r) // 2
            s = mid * mid
            if s == num:
                return True
            elif s < num:
                l = mid + 1
            else:
                r = mid - 1
        return False
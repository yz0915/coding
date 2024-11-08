# 278. First Bad Version: [G G B B G G]
# https://leetcode.com/problems/first-bad-version/

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l, r = 1, n
        ans = -1
        while l <= r:
            mid = (l + r) // 2
            if isBadVersion(mid):
                r = mid - 1
                ans = mid
            else:
                l = mid + 1
        return ans

def isBadVersion(n):
    return False
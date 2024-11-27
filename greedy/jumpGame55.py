# 55. Jump Game
# https://leetcode.com/problems/jump-game/description/

def canJump(nums):
    n = len(nums)
    to_max = 0

    for i in range(n):
        if i > to_max:
            return False

        to_max = max(to_max, i + nums[i])

        if to_max >= n - 1:
            return True

    return False
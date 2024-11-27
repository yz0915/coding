# lc 45 Jump Game II
# https://leetcode.com/problems/jump-game-ii/

# Input: nums = [2,3,1,1,4]
# Output: 2
# Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.

# why greedy: at every step, it makes a locally optimal choice — that is, it tries to extend the farthest possible range (to_max) that can be reached at that point in time.
def jump(nums):
    n = len(nums)
    to_max = 0
    current = 0
    jumps = 0

    for i in range(n - 1):
        to_max = max(to_max, i + nums[i])
        if i == current:
            jumps += 1
            current = to_max

    return jumps
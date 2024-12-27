# lc 213
# https://leetcode.com/problems/house-robber-ii/

# House Robber I + All houses at this place are arranged in a circle


def rob(nums):
    return max(nums[0], helper(nums[1:]), helper(nums[:-1]))

def helper(self, nums):
    rob1, rob2 = 0, 0

    for n in nums:
        newRob = max(rob1 + n, rob2)
        rob1 = rob2
        rob2 = newRob
    return rob2
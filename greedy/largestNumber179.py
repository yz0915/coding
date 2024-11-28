# lc 179
# https://leetcode.com/problems/largest-number/

# Input: nums = [10,2]
# Output: "210"

# Input: nums = [00,0]
# Output: "0"

def largestNumber(nums):
    def isSwap(s1, s2):
        return int(s1 + s2) < int(s2 + s1)

    origin = nums[:]
    nums = [str(n) for n in nums]
    n = len(nums)
    
    for i in range(n):
        for j in range(i + 1, n):
            if isSwap(nums[i], nums[j]):
                nums[i], nums[j] = nums[j], nums[i]
    
    return ''.join(nums) if sum(origin) else '0'
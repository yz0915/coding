# 31. Next Permutation
# https://leetcode.com/problems/next-permutation/

# 12[3]654 -> 124[653] -> 124356
# 321 -> 123

def nextPermutation(nums):
    n = len(nums)

    # 1. Find the largest index `j` such that nums[j] < nums[j + 1]. If no such index exists, reverse and return.
    j = n - 2
    while j >= 0 and nums[j] >= nums[j + 1]:
        j -= 1

    # 2. If such an index `j` exists, find the largest index `l > j` such that nums[j] < nums[l].
    if j >= 0:
        l = n - 1
        while nums[l] <= nums[j]:
            l -= 1
        # Swap nums[j] and nums[l]
        nums[j], nums[l] = nums[l], nums[j]

    # 3. Reverse the subarray nums[j + 1:] to get the next permutation.
    nums[j + 1:] = reversed(nums[j + 1:])
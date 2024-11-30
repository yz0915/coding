# lc 228
# https://leetcode.com/problems/summary-ranges/

'''
Input: nums = [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
Explanation: The ranges are:
[0,2] --> "0->2"
[4,5] --> "4->5"
[7,7] --> "7"
'''

def summaryRanges(nums):
    num_set = set(nums)

    result = []
    start = None
    end = None

    for num in nums:
        # Check if num-1 and num+1 exist in the set
        prev_exists = (num - 1) in num_set
        next_exists = (num + 1) in num_set

        if not prev_exists and not next_exists:  # Single point
            result.append(str(num))
            continue

        if not prev_exists:  # Start of a range
            start = num
        if not next_exists:  # End of a range
            end = num
            result.append(f"{start}->{end}")

    return result
# 528. Random Pick Index with Weight: // [1,2,3,4] => [1 2 3 10]
# https://leetcode.com/problems/random-pick-with-weight/

import random
import bisect

class Solution:
    def __init__(self, w):
        self.nums = []
        prefix_sum = 0
        for weight in w:
            prefix_sum += weight
            self.nums.append(prefix_sum)

    def pickIndex(self):
        # Generate a random number in the range [0, total_sum - 1]
        r = random.randint(0, self.nums[-1] - 1)
        # Use binary search to find the index
        return bisect.bisect_right(self.nums, r)


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
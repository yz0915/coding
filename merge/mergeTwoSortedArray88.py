# merge solves leetcode 88 https://leetcode.com/problems/merge-sorted-array/description/
# nums1=[4 5 6 0 0 0], nums2=[1 2 3] => [1 2 3 4 5 6]

class Solution:
    def merge(self, nums1, m: int, nums2, n):
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1 = m - 1
        p2 = n - 1
        i = m + n - 1
        while p2 >= 0:
            if p1 >= 0 and nums1[p1] > nums2[p2]:
                nums1[i] = nums1[p1]
                p1 -= 1
                i -= 1
            else:
                nums1[i] = nums2[p2]
                p2 -= 1
                i -= 1
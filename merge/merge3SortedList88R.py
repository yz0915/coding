# https://leetcode.com/problems/merge-sorted-array/
# Merge nums1=[1,3,5,7], nums2=[2,4,6,9], nums3= [1,3,6,7] without duplicates => [1 2 3 4 5 6 7 9]

def merge(self, nums1, m, nums2, n):
    """
    Do not return anything, modify nums1 in-place instead.
    """
    while m > 0 and n > 0:
        if nums1[m-1] >= nums2[n-1]:
            nums1[m+n-1] = nums1[m-1]
            m -= 1
        else:
            nums1[m+n-1] = nums2[n-1]
            n -= 1
    if n > 0:
        nums1[:n] = nums2[:n]
#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#
# https://leetcode.com/problems/median-of-two-sorted-arrays/description/
#
# algorithms
# Hard (28.34%)
# Total Accepted:    593.9K
# Total Submissions: 2.1M
# Testcase Example:  '[1,3]\n[2]'
#
# There are two sorted arrays nums1 and nums2 of size m and n respectively.
# 
# Find the median of the two sorted arrays. The overall run time complexity
# should be O(log (m+n)).
# 
# You may assume nums1 and nums2 cannot be both empty.
# 
# Example 1:
# 
# 
# nums1 = [1, 3]
# nums2 = [2]
# 
# The median is 2.0
# 
# 
# Example 2:
# 
# 
# nums1 = [1, 2]
# nums2 = [3, 4]
# 
# The median is (2 + 3)/2 = 2.5
# 
# 
#
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        len1 = len(nums1)
        len2 = len(nums2)
        middle = int((len1 + len2) / 2) + 1
        odd, even = False, False
        if (len1 + len2) % 2:
            middle = middle - 1
            odd = True
        else: 
            middle = middle - 2 
            even = True
        i = 0
        while i < middle:
            if not nums1:
                del nums2[0]
                i = i + 1 
                continue
            elif not nums2:
                del nums1[0]
                i = i + 1
                continue
            if nums1[0] < nums2[0]:
                del nums1[0]
            else:
                del nums2[0]
            i = i + 1
        if even:
            if not nums1:
                ans = (nums2[0] + nums2[1]) / 2
            elif not nums2:
                ans = (nums1[0] + nums1[1]) / 2
            else: 
                if len(nums1) > 1 and nums1[1] < nums2[0]:
                    ans = (nums1[0] + nums1[1]) / 2
                elif len(nums2) > 1 and nums2[1] < nums1[0]:
                    ans = (nums2[0] + nums2[1]) / 2
                else:
                    ans = (nums1[0] + nums2[0]) / 2
        else:
            if not nums1:
                ans = nums2[0]
            elif not nums2:
                ans = nums1[0]
            else:
                ans = min(nums1[0], nums2[0])
        return ans
        

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
        i, i1, i2 = 0, 0, 0
        i1_fin, i2_fin = False, False
        last1, last2 = 0, 0
        while i < middle:
            i = i + 1
            if i1 == len1:
                i1_fin = True
            elif i2 == len2:
                i2_fin = True
            if i1_fin:
                last2 = last1
                last1 = nums2[i2]
                i2 = i2 + 1 
                continue
            elif i2_fin:
                last2 = last1
                last1 = nums1[i1]
                i1 = i1 + 1 
                continue
            if nums1[i1] < nums2[i2]:
                last2 = last1
                last1 = nums1[i1]
                i1 = i1 + 1 
            else:
                last2 = last1
                last1 = nums2[i2]
                i2 = i2 + 1 

        if (len1 + len2) % 2 == 0:
            ans = (last1 + last2) / 2
        else:
            ans = last1
        return ans
        

#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
       max = 0
       left = 0
       right = len(height) - 1
       while left < right:
           volume = min(height[left], height[right]) * (right - left) 
           if volume > max:
               max = volume
           if height[left] < height[right]:
               left = left + 1
           else:
               right = right - 1 
       return max
           

# @lc code=end


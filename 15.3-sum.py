#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sNums = sorted(nums)
        ans = []
        n = len(nums)
        if n < 3:
            return ans
        i = 0
        a = sNums[i]
        while a <= 0 and i < n:
            start = i+1
            end = n-1
            a = sNums[i]
            while start < end:
                b, c = sNums[start], sNums[end]
                if a+b+c == 0:
                    ans.append([a,b,c])
                    while c == sNums[end] and end > start:
                        end = end - 1
                elif a+b+c > 0:
                    while c == sNums[end] and end > start:
                        end = end - 1
                else:
                    while b == sNums[start] and end > start:
                        start = start + 1
            while a == sNums[i]:
                i = i + 1
                if i == n:
                    break
        return ans
                    
        
# @lc code=end


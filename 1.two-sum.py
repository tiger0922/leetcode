#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        ans = []
        for i in range(len(nums)):
            if dict.get(target-nums[i]) != None:
                ans.append(dict.get(target-nums[i]))
                ans.append(i)
                return ans
            else:
                dict[nums[i]] = i
        return ans
# @lc code=end


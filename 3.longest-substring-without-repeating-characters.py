#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max = 0
        longest = []
        for i in range(len(s)):
            if s[i] not in longest:
                longest.append(s[i])
                if len(longest) > max:
                    max = len(longest)
            else:
                del longest[:longest.index(s[i])+1]
                longest.append(s[i])
        return max


        
# @lc code=end


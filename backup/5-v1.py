#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        max = 0
        ans = ""
        # odd
        for i in range(len(s)):
            j = 0 
            try:
                while s[i-j] == s[i+j] and i - j >= 0:
                    if j * 2 + 1 > max:
                        max = j * 2 + 1
                        ans = s[i-j:i+j+1]
                    j = j + 1
            except:
                continue
        # even
        for i in range(len(s)):
            j = 0
            try:
                while s[i-j] == s[i+1+j] and i - j >= 0:
                    if (j+1) * 2 > max:
                        max = (j+1) * 2
                        ans = s[i-j:i+j+2]
                    j = j + 1
            except:
                continue
        return ans

        
# @lc code=end


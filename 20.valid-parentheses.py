#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        last = ""
        for i in range(len(s)):
            if s[i] == '(': last = last + '(' 
            elif s[i] == '[': last = last + '['
            elif s[i] == '{': last = last + '{'
            elif len(last) > 0:
                if s[i] == ')' and last[-1] == '(': last = last[:-1]  
                elif s[i] == ']' and last[-1] == '[': last = last[:-1] 
                elif s[i] == '}' and last[-1] == '{': last = last[:-1]
                else: return False
            else: return False
        return not last
        
# @lc code=end


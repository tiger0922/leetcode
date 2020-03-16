#
# @lc app=leetcode id=10 lang=python3
#
# [10] Regular Expression Matching
#

# @lc code=start
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if not s and not p:
            return True
        elif len(s) == 1 and len(p) == 1:
            if s[0] == p[0] or p[0] == '.':
                return True
            else:
                return False
        elif len(p) > 1 and p[1] != '*':
            if not s:
                return False
            elif s[0] == p[0] or p[0] == '.':
                return self.isMatch(s[1:], p[1:]) 
            else:
                return False
        elif len(p) > 1 and p[1] == '*':
            if(self.isMatch(s, p[2:])): 
                return True
            if len(s) > 0 and (s[0] == p[0] or p[0] == '.'):
                return self.isMatch(s[1:], p)
        else:
            return False

    
# @lc code=end


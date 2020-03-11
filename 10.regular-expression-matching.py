#
# @lc app=leetcode id=10 lang=python3
#
# [10] Regular Expression Matching
#

# @lc code=start
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        s_pos, p_pos = 0, 0
        ch_star = ''
        fail = False
        while fail == False and s_pos < len(s) and p_pos < len(p):
            if s[s_pos] == p[p_pos] or p[p_pos] == '.':
                s_pos = s_pos + 1 
                p_pos = p_pos + 1
            elif p[p_pos] == '*':
                ch_star = p[p_pos-1]
                if s[s_pos] != ch_star and ch_star != '.':
                    p_pos = p_pos + 1
                else:
                    s_pos = s_pos + 1
            elif p_pos + 1 < len(p) and p[p_pos+1] == "*":
                p_pos = p_pos + 1
            else:
                fail = True
        if (p_pos != len(p) or s_pos != len(s)) and p[-1] != "*" and ch_star != '.' and ch_star != s[-1]:
            fail = True
        elif ch_star == '.' and p[-1] != s[-1] and p[-1] != "*":
            fail = True
        if s_pos < len(s):
            if s[s_pos] != ch_star and p[-1] == "*":
                fail = True

        return not fail
    
# @lc code=end


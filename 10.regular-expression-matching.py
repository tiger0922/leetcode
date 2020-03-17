#
# @lc app=leetcode id=10 lang=python3
#
# [10] Regular Expression Matching
#

# @lc code=start
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # Initialize
        dp = [[False for i in range(len(p)+1)] for j in range(len(s)+1)]
        dp[0][0] = True
        for j in range(1, len(p)+1):
            if j > 1 and p[j-1] == '*' and dp[0][j-2] == True:
                dp[0][j] = True
        
        # Start filling 
        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                if p[j-1] == '*':
                    dp[i][j] = (s[i-1] == p[j-2] or p[j-2] == '.') and dp[i-1][j] or dp[i][j-2]
                else:
                    dp[i][j] = (s[i-1] == p[j-1] or p[j-1] == '.') and dp[i-1][j-1]

        return dp[-1][-1]

    
# @lc code=end


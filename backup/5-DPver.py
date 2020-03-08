class Solution:
    def longestPalindrome(self, s: str) -> str:
        dp = [[False for i in range(len(s))] for j in range(len(s))]
        maxLeng = 0
        ans = ""
        for i in reversed(range(len(s))):
            for j in range(i, len(s)):
                if j == i:
                    dp[i][j] = True
                elif j == i + 1 and s[j] == s[i]:
                    dp[i][j] = True
                elif dp[i+1][j-1] and s[j] == s[i]:
                    dp[i][j] = True
                if j-i+1 > maxLeng and dp[i][j]:
                    ans = s[i:j+1]
                    maxLeng = j-i+1
        return ans

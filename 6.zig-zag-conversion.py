#
# @lc app=leetcode id=6 lang=python3
#
# [6] ZigZag Conversion
#

# @lc code=start
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        strList = []
        index = 0
        ans = ""
        for i in range(numRows):
            strList.append("")
        while index < len(s):
            for j in range(numRows): 
                if index == len(s):
                    break
                strList[j] = strList[j] + s[index]
                index = index + 1
            for k in range(numRows-2, 0, -1):
                if index == len(s):
                    break
                strList[k] = strList[k] + s[index]
                index = index + 1
        for i in range(len(strList)):
            ans = ans + strList[i]
        return ans
        
# @lc code=end


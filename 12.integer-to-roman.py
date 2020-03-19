#
# @lc app=leetcode id=12 lang=python3
#
# [12] Integer to Roman
#

# @lc code=start
class Solution:
    def intToRoman(self, num: int) -> str:
        ans = ''
        while num >= 1000:
            num = num - 1000
            ans = ans + 'M'
        while num >= 100:
            if num >= 900:
                num = num - 900
                ans = ans + "CM"
            elif num >= 500 and num < 900:
                num = num - 500
                ans = ans + "D"
            elif num >= 400 and num < 500:
                num = num - 400
                ans = ans + "CD"
            else:
                num = num - 100
                ans = ans + 'C'
        while num >= 10:
            if num >= 90:
                num = num - 90
                ans = ans + "XC"
            elif num >= 50 and num < 90:
                num = num - 50
                ans = ans + "L"
            elif num >= 40 and num < 50:
                num = num - 40
                ans = ans + "XL"
            else:
                num = num - 10
                ans = ans + 'X'
        while num >= 1:
            if num >= 9:
                num = num - 9
                ans = ans + "IX"
            elif num >= 5 and num < 9:
                num = num - 5
                ans = ans + "V"
            elif num >= 4 and num < 5:
                num = num - 4
                ans = ans + "IV"
            else:
                num = num - 1
                ans = ans + 'I'
        return ans
        
# @lc code=end


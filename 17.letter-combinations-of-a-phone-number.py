#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#

# @lc code=start
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        amount = 1
        letter = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        for i in range(len(digits)):
            amount = amount * len(letter[int(digits[i])]) 
        ans = [""] * amount
        i, j = 0, 0
        division = 1
        if len(digits) == 0:
            return [] 
        while i < len(digits):
            leng = len(letter[int(digits[i])])
            division = division * leng
            for j in range(amount):
                ans[j] = ans[j] + letter[int(digits[i])][j//(amount//division)%leng]
            i = i + 1
        return ans
# @lc code=end


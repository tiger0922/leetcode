#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#

# @lc code=start
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0: return []
        character = {2:"abc", 3:"def", 4:"ghi", 5:"jkl", 6:"mno", 7:"pqrs", 8:"tuv", 9:"wxyz"}
        ans = []
        self.solve(digits, character, ans)
        return ans 
    def solve(self, digits, character, ans, current_level = 0, current_str = ""):
        if current_level == len(digits):
            ans.append(current_str)
            return 
        for c in character[int(digits[current_level])]:
            self.solve(digits, character, ans, current_level+1, current_str+c)
# @lc code=end


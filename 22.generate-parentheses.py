#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#

# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        self.solve(ans, n, 0, 0)
        return ans
    def solve(self, ans, n, left_num, right_num, current_str=""):
        if left_num == right_num == n:
            ans.append(current_str)
            return
        if left_num == 0:
            self.solve(ans, n, left_num+1, right_num, current_str+'(')
        elif left_num == n:
            self.solve(ans, n, left_num, right_num+1, current_str+')')
        elif left_num > right_num:
            self.solve(ans, n, left_num, right_num+1, current_str+')')
            self.solve(ans, n, left_num+1, right_num, current_str+'(')
        else:
            self.solve(ans, n, left_num+1, right_num, current_str+'(')
# @lc code=end


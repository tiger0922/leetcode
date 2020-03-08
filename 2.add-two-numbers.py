#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        sum = ListNode(0)
        if l1 or l2:
            if l1 == None:
                l1 = ListNode(0)
            elif l2 == None:
                l2 = ListNode(0)
            add = l1.val + l2.val 
            sum.val = add%10
            carry = 1 if add >= 10 else 0
            if carry:
                if l1.next == None:
                    l1.next = ListNode(0)
                l1.next.val += 1
            sum.next = self.addTwoNumbers(l1.next, l2.next)
        elif sum.val == 0:
            return None 
        return sum
        
# @lc code=end


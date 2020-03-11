#
# @lc app=leetcode id=24 lang=python3
#
# [24] Swap Nodes in Pairs
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        current = head
        if current == None: return current
        head = current.next
        if head == None: return current
        stay = None
        while current != None:
            left = current
            right = current.next
            if right == None:
                break
            temp = right.next
            right.next = left
            left.next = temp
            if stay != None:
                stay.next = right
            current = temp
            if temp == None:
                break
            stay = left
        return head
            
        
# @lc code=end


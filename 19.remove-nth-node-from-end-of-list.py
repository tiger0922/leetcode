#
# @lc app=leetcode id=19 lang=python3
#
# [19] Remove Nth Node From End of List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        target = None
        current = head
        i = 1
        while current != None:
            if i > n and target == None: 
                target = head
            elif target != None:
                target = target.next
            current = current.next
            i = i + 1
        if target == None: 
            head = head.next
        else:
            target.next = target.next.next
        return head
        
# @lc code=end


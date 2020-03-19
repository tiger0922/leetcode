#
# @lc app=leetcode id=23 lang=python3
#
# [23] Merge k Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        min = lists[0].val
        min_id = 0
        for i in range(len(lists)):
            if lists[i].val < min:
                min = lists[i].val
                min_id = i
        head = lists[min_id]
        lists[min_id] = lists[min_id].next
        while True:
            min_id = 0
            for i in range(len(lists)):
                if lists[i] != None: min = lists[i].val
                else: continue
            if min == None: break
            for i in range(len(lists)):
                if lists[i] != None and lists[i].val < min:
                    min = lists[i].val 
                    min_id = i
            head.Next = lists[min_id] 
            if lists[min_id] != None:
                lists[min_id] = lists[min_id].next
        return head
                
        
# @lc code=end


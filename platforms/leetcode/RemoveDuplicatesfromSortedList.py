# https://leetcode.com/problems/remove-duplicates-from-sorted-list/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head: return None
        prev, next = head, head.next
        while next:
            if next.val == prev.val:
                prev.next = next.next
                next = next.next
            else:
                prev, next = next, next.next
        return head

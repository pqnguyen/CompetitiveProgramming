# https://leetcode.com/problems/remove-linked-list-elements/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        while head and head.val == val: head = head.next
        if not head: return None
        prev, next = head, head.next
        while next:
            if next.val == val:
                prev.next = next.next
                next = next.next
            else:
                prev, next = next, next.next
        return head

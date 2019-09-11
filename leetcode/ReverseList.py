# https://leetcode.com/problems/reverse-linked-list/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next: return head
        prev, next = head, head.next
        prev.next = None
        while next:
            tmp = next.next
            next.next = prev
            prev, next = next, tmp
        return prev

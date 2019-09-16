# https://leetcode.com/explore/learn/card/linked-list/219/classic-problems/1208/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head: return None
        second = head.next
        prev, cur = None, head
        while cur:
            if prev:
                prev.next = cur.next
            prev = cur
            cur = cur.next
        first = head
        while first and first.next: first = first.next
        first.next = second
        return head

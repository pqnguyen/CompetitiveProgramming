# https://leetcode.com/problems/merge-two-sorted-lists/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head, tail = None, None
        while l1 and l2:
            if l1.val < l2.val:
                node = l1
                l1 = l1.next
            else:
                node = l2
                l2 = l2.next
            if not head:
                head = tail = node
            else:
                tail.next = node
                tail = node

        lastNode = l1 if l1 else l2
        if tail:
            tail.next = lastNode
        else:
            head = lastNode

        return head

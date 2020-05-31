# https://leetcode.com/explore/learn/card/linked-list/213/conclusion/1295/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or k == 0: return head
        last, length = self.getLength(head)
        k = k % length
        if not k: return head
        next = head
        for i in range(length - k - 1):
            next = next.next
        tmp = next.next
        next.next = None
        last.next = head
        return tmp

    def getLength(self, head):
        length = 0
        while head and head.next:
            length += 1
            head = head.next
        if head: length += 1
        return head, length

# https://leetcode.com/explore/learn/card/linked-list/213/conclusion/1225/
"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""


class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        self.last = None
        self.flattenUtil(head)
        return head

    def flattenUtil(self, head):
        if not head: return
        self.last = head
        next = head.next
        if head.child:
            self.flattenUtil(head.child)
            head.next = head.child
            head.child.prev = head
            head.child = None
        if self.last != head:
            self.last.next = next
            if next:
                next.prev = self.last
        self.flattenUtil(next)

# https://leetcode.com/explore/learn/card/linked-list/213/conclusion/1228/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        self.head = self.tail = None
        carry = 0

        while l1 or l2:
            s = carry
            if l1:
                s += l1.val
                l1 = l1.next

            if l2:
                s += l2.val
                l2 = l2.next

            val, carry = s % 10, s // 10
            self.insert(val)

        if carry: self.insert(carry)
        return self.head

    def insert(self, val):
        node = ListNode(val)
        if not self.tail:
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node

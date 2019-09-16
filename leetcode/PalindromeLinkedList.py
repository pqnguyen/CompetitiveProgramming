# https://leetcode.com/explore/learn/card/linked-list/219/classic-problems/1209/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head: return True
        mid = self.findMid(head)
        lastNode = self.reverse(mid)
        while lastNode:
            if head.val != lastNode.val: return False
            lastNode = lastNode.next
            head = head.next
        return True

    def reverse(self, head):
        if not head: return None
        prev, next = head, head.next
        while next:
            tmp = next.next
            next.next = prev
            prev = next
            next = tmp
        head.next = None
        return prev

    def findMid(self, head):
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        if fast:
            tmp = slow.next
            slow.next = None
            slow = tmp
        return slow

# https://leetcode.com/explore/learn/card/linked-list/214/two-pointer-technique/1215/
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        la, tailA = self.getLength(headA)
        lb, tailB = self.getLength(headB)
        if tailA != tailB: return None
        while la > lb:
            headA = headA.next
            la -= 1
        while lb > la:
            headB = headB.next
            lb -= 1

        while headA != headB:
            headA = headA.next
            headB = headB.next
        return headA

    def getLength(self, head):
        length = 0
        while head and head.next:
            length += 1
            head = head.next
        if head: length += 1
        return length, head

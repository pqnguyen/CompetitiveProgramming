# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def reverseList(self, A):
        if not A or not A.next: return A
        prev, next = A, A.next
        while next:
            morenext = next.next
            next.next = prev
            prev = next
            next = morenext
        A.next = None
        return prev

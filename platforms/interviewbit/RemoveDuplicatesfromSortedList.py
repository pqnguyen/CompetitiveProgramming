# Definition for singly-linked list.
# class ListNode:
#	def __init__(self, x):
#		self.val = x
#		self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def deleteDuplicates(self, A):
        current = A
        while current:
            if not current.next or current.val != current.next.val:
                current = current.next
            else:
                next = current.next
                while next and next.val == current.val: next = next.next
                current.next = next
                current = next
        return A

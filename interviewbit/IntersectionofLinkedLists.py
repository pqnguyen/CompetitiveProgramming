# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    # @param A : head node of linked list
    # @param B : head node of linked list
    # @return the head node in the linked list
    def getIntersectionNode(self, A, B):
        lengthA, lastNodeA = self.length(A)
        lengthB, lastNodeB = self.length(B)
        if lastNodeA != lastNodeB:
            return None
        while lengthA > lengthB:
            lengthA -= 1
            A = A.next

        while lengthB > lengthA:
            lengthB -= 1
            B = B.next

        while A != B:
            A = A.next
            B = B.next

        return A

    def length(self, A):
        if not A: return 0, None
        length = 0
        while A.next:
            length += 1
            A = A.next
        return length + 1, A

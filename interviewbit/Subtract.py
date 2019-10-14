# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from collections import deque


class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def subtract(self, A):
        stack = deque()
        mid = self.findMiddle(A)
        current = mid
        while current:
            stack.append(current.val)
            current = current.next
        current = A
        while current != A:
            current.val = stack.pop() - current.val
            current = current.next
        return A

    def findMiddle(self, head):
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow


A = [1, 2, 3]
res = Solution().subtract(A)
print(res)

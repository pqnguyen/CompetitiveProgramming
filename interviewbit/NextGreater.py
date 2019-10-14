# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from collections import deque


class Solution:
    # @param A : list of integers
    # @return a list of integers
    def nextGreater(self, A):
        stack = deque()
        res = [-1] * len(A)
        for i in range(len(A) - 1, -1, -1):
            while stack and A[i] >= stack[-1]: stack.pop()
            if stack: res[i] = stack[-1]
            stack.append(A[i])
        return res


A = [1, 2, 3]
res = Solution().nextGreater(A)
print(res)

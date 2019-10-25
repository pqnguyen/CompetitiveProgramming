# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
import heapq


class Solution:
    # @param A : list of linked list
    # @return the head node in the linked list
    def mergeKLists(self, A):
        fakehead = tail = ListNode(0)
        pq = []
        for node in A: self.push(pq, node)
        while pq:
            top = self.pop(pq)
            tail.next = top
            tail = top
            if top.next:
                self.push(pq, top.next)
        return fakehead.next

    def push(self, pq, node):
        heapq.heappush(pq, (node.val, node))

    def pop(self, pq):
        return heapq.heappop(pq)[1]

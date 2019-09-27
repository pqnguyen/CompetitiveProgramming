# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

import heapq


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        heap = []
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i))
                lists[i] = node.next

        head = tail = None

        def insertNode(head, tail, val):
            node = ListNode(smallestVal)
            if tail is None:
                head = tail = node
            else:
                tail.next = node
                tail = node
            return head, tail

        while heap:
            smallestVal, index = heapq.heappop(heap)
            head, tail = insertNode(head, tail, smallestVal)
            nextNode = lists[index]
            if nextNode:
                heapq.heappush(heap, (nextNode.val, index))
                lists[index] = nextNode.next

        return head

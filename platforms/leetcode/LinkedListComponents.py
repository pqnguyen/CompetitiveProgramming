# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def numComponents(self, head: ListNode, G: List[int]) -> int:
        g = set(G)
        res = 0
        isComponent = False
        while head:
            if head.val in g:
                isComponent = True
            else:
                if isComponent:
                    res += 1
                isComponent = False
            head = head.next
        if isComponent: res += 1

        return res
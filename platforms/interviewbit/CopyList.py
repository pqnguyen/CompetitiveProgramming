# Definition for singly-linked list with a random pointer.
# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None


class Solution:
    # @param head, a RandomListNode
    # @return a RandomListNode
    def copyRandomList(self, head):
        tb = {None: None}
        current = head
        while current:
            node = RandomListNode(current.label)
            tb[current] = node
            current = current.next

        fakeHead = fakeTail = RandomListNode(0)
        fakeHead.next = head
        current = head
        while current:
            fakeTail.next = tb[current]
            fakeTail.next.random = tb[current.random]
            fakeTail = fakeTail.next
            current = current.next
        return fakeHead.next

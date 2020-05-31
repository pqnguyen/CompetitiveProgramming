# https://leetcode.com/explore/learn/card/linked-list/213/conclusion/1229/
"""
# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        m = {}
        cloneHead = self.deepCopy(head, m)
        return cloneHead

    def deepCopy(self, head, m):
        if not head: return None
        node = Node(head.val, None, None)
        m[head] = node
        nextNode = self.deepCopy(head.next, m)
        node.next = nextNode
        if head.random:
            node.random = m[head.random]
        return node

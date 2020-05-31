# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque


class BSTIterator:
    # @param root, a binary search tree's root node
    def __init__(self, root):
        self.stack = deque()
        current = root
        while current:
            self.stack.append(current)
            current = current.left

    # @return a boolean, whether we have a next smallest number
    def hasNext(self):
        return self.stack

    # @return an integer, the next smallest number
    def next(self):
        node = self.stack.pop()
        current = node.right
        while current:
            self.stack.append(current)
            current = current.left
        return node.val

# Your BSTIterator will be called like this:
# i = BSTIterator(root)
# while i.hasNext(): print i.next(),

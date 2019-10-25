# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None
from collections import deque


class Solution:
    # @param A : root node of tree
    # @return a list of list of integers
    def zigzagLevelOrder(self, A):
        if not A: return []
        level = 0
        parents = [A.head]
        res = []
        while parents:
            parentsValue = [parent.val for parent in parents]
            if level % 2 == 0:
                res.append(parentsValue)
            else:
                res.append(list(reversed(parentsValue)))

            children = []
            for parent in parents:
                if parent.left:
                    children.append(parent.left)
                if parent.right:
                    children.append(parent.right)
            parents = children
            level += 1

        return res

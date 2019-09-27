# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque


class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        if not root: return 0
        parents = deque([root])
        res = (0, 0)
        level = 1
        while parents:
            total = 0
            children = deque()
            for parent in parents:
                total += parent.val
                if parent.left: children.append(parent.left)
                if parent.right: children.append(parent.right)
            if total > res[1]: res = (level, total)
            level += 1
            parents = children
        return res[0]

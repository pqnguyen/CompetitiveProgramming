# https://leetcode.com/problems/minimum-depth-of-binary-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root: return 0
        queue = deque([(root, 1)])
        while queue:
            top, level = queue.popleft()
            if not top.left and not top.right: return level
            if top.left:
                queue.append((top.left, level + 1))
            if top.right:
                queue.append((top.right, level + 1))
        return 0

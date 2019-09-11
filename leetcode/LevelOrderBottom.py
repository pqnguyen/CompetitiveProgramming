# https://leetcode.com/problems/binary-tree-level-order-traversal-ii/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque


class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        parents = deque([root])
        res = []
        level = 0
        while parents:
            children = deque()
            res.append([])
            while parents:
                parent = parents.popleft()
                res[level].append(parent.val)
                if parent.left:
                    children.append(parent.left)
                if parent.right:
                    children.append(parent.right)
            parents = children
            level += 1
        res.reverse()
        return res

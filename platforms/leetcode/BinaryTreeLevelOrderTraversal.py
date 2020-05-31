# https://leetcode.com/explore/learn/card/data-structure-tree/134/traverse-a-tree/931/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        res = []
        parents = [root]
        while parents:
            level, children = [], []
            for parent in parents:
                level.append(parent.val)
                if parent.left: children.append(parent.left)
                if parent.right: children.append(parent.right)
            res.append(level)
            parents = children
        return res

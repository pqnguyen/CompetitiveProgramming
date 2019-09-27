# https://leetcode.com/explore/learn/card/data-structure-tree/133/conclusion/932/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        path2p, path2q = [], []
        self.findPath(root, p.val, path2p)
        self.findPath(root, q.val, path2q)
        index = 0
        if len(path2p) < len(path2q):
            path2p.append(None)
        else:
            path2q.append(None)
        while path2p[index] == path2q[index]: index += 1
        return path2p[index - 1]

    def findPath(self, root, val, path):
        if not root: return False
        path.append(root)
        if root.val == val: return True
        if self.findPath(root.left, val, path): return True
        if self.findPath(root.right, val, path): return True
        path.pop()
        return False

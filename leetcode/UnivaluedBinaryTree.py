# https://leetcode.com/problems/univalued-binary-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        if not root: return True
        return self.isUnivalTreeUtil(root, root.val)

    def isUnivalTreeUtil(self, root, val):
        if not root: return True
        if root.val != val:
            return False
        if not self.isUnivalTreeUtil(root.left, val):
            return False
        return self.isUnivalTreeUtil(root.right, val)

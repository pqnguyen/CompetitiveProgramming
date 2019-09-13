# https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        return self.sumRootToLeafUtil(root, 0)

    def sumRootToLeafUtil(self, root, v):
        if not root: return 0
        v = (v << 1) | root.val
        if not root.left and not root.right:
            return v
        res = 0
        if root.left:
            res += self.sumRootToLeafUtil(root.left, v)
        if root.right:
            res += self.sumRootToLeafUtil(root.right, v)
        return res

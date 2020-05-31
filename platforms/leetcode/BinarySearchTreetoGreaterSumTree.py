# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        self.current_sum = 0
        self.bstToGstUtil(root)
        return root

    def bstToGstUtil(self, root):
        if not root: return
        self.bstToGstUtil(root.right)
        self.current_sum += root.val
        root.val = self.current_sum
        self.bstToGstUtil(root.left)

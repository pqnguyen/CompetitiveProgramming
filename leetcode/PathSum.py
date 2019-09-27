# https://leetcode.com/explore/learn/card/data-structure-tree/17/solve-problems-recursively/537/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root: return False
        if not root.left and not root.right and root.val == sum:
            return True
        if self.hasPathSum(root.left, sum - root.val): return True
        return self.hasPathSum(root.right, sum - root.val)

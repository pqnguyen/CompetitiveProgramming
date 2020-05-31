# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return an integer
    def hasPathSum(self, A, B):
        return 1 if self.hasPathSumHelper(A, 0, B) else 0

    def hasPathSumHelper(self, node, sum, target):
        if not node: return False
        if not node.left and not node.right and sum + node.val == target:
            return True
        if self.hasPathSumHelper(node.left, sum + node.val, target):
            return True
        if self.hasPathSumHelper(node.right, sum + node.val, target):
            return True
        return False

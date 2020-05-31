# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @return an integer
    def maxDepth(self, A):
        return self.maxDepthHelper(A)

    def maxDepthHelper(self, node):
        if not node: return 0
        return max(self.maxDepthHelper(node.left), self.maxDepthHelper(node.right)) + 1

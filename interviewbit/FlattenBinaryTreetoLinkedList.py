# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @return the root node in the tree
    def flatten(self, A):
        self.pre = None
        self.flattenHelper(A)
        return A

    def flattenHelper(self, node):
        if not node: return None
        self.flattenHelper(node.right)
        self.flattenHelper(node.left)
        node.right = self.pre
        node.left = None
        self.pre = node

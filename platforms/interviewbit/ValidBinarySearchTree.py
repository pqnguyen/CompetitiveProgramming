# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @return an integer
    def isValidBST(self, A):
        if self.isValidBSTHelper(A, -2 ** 31, 2 ** 31 - 1):
            return 1
        return 0

    def isValidBSTHelper(self, node, left, right):
        if not node: return True
        if node.val <= left or node.val >= right: return False
        if not self.isValidBSTHelper(node.left, left, node.val) or not self.isValidBSTHelper(node.right, node.val,
                                                                                             right):
            return False
        return True

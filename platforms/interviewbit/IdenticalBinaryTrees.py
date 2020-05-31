# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @param B : root node of tree
    # @return an integer
    def isSameTree(self, A, B):
        return 1 if self.isSameTreeHelper(A, B) else 0

    def isSameTreeHelper(self, A, B):
        if not A and not B: return True
        if not A and B: return False
        if A and not B: return False
        if A.val != B.val: return False
        return self.isSameTreeHelper(A.left, B.left) and self.isSameTreeHelper(A.right, B.right)

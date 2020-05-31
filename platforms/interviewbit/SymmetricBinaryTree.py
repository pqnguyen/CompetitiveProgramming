# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None
from collections import defaultdict


class Solution:
    # @param A : root node of tree
    # @return an integer
    def isSymmetric(self, A):
        if not A or self.isSymmetricHelper(A.left, A.right):
            return 1
        return 0

    def isSymmetricHelper(self, A, B):
        if not A or not B: return A == B
        if A.val != B.val: return False
        return self.isSymmetricHelper(A.left, B.right) and self.isSymmetricHelper(A.right, B.left)

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
    def kthsmallest(self, A, K):
        self.k = 0
        return self.kthsmallestHelper(A, K)

    def kthsmallestHelper(self, node, k):
        if not node: return None
        val = self.kthsmallestHelper(node.left, k)
        if val: return val
        self.k += 1
        if self.k == k: return node.val
        return self.kthsmallestHelper(node.right, k)

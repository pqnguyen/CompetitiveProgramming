# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None

class Solution:
    # @param A : root node of tree
    # @return an integer
    def isBalanced(self, A):
        res, _ = self.isBalancedHelper(A)
        return res

    def isBalancedHelper(self, A):
        if not A: return True, 0
        isBalancedLeft, heightLeft = self.isBalancedHelper(A.left)
        if not isBalancedLeft: return False, heightLeft
        isBalancedRight, heightRight = self.isBalancedHelper(A.right)
        if not isBalancedRight: return False, heightRight
        return abs(heightLeft - heightRight) <= 1, max(heightLeft, heightRight) + 1

# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @return an integer
    def sumNumbers(self, A):
        return self.sumNumbersHelper(A, 0) % 1003

    def sumNumbersHelper(self, node, num):
        if not node: return num % 1003
        num = num * 10 + node.val
        if node.left and not node.right:
            return self.sumNumbersHelper(node.left, num)
        if node.right and not node.left:
            return self.sumNumbersHelper(node.right, num)
        if not node.left and not node.right:
            return num % 1003
        return (self.sumNumbersHelper(node.left, num) + self.sumNumbersHelper(node.right, num)) % 1003

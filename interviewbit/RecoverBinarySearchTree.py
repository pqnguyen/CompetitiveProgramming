# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def recoverTree(self, A):
        self.pre = self.first = self.second = None
        self.recoverTreeHelper(A, -2 ** 31, 2 ** 31 - 1)
        if not self.first: return []
        return [self.second, self.first]

    def recoverTreeHelper(self, node, left, right):
        if not node: return
        self.recoverTreeHelper(node.left, left, node.val)
        if not self.pre:
            self.pre = node.val
        else:
            if node.val < self.pre:
                if not self.first:
                    self.first = self.pre
                self.second = node.val
            self.pre = node.val
        self.recoverTreeHelper(node.right, node.val, right)

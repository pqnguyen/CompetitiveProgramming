# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : list of integers
    # @return the root node in the tree
    def buildTree(self, A):
        return self.buildTreeHelper(A, 0, len(A) - 1)

    def buildTreeHelper(self, a, start, end):
        if start > end: return None
        idx = self.findMaxIndex(a, start, end)
        node = TreeNode(a[idx])
        node.left = self.buildTreeHelper(a, start, idx - 1)
        node.right = self.buildTreeHelper(a, idx + 1, end)
        return node

    def findMaxIndex(self, a, start, end):
        if start > end: return -1
        res = start
        for i in range(start, end + 1):
            if a[i] > a[res]:
                res = i
        return res

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : tuple of integers
    # @return the root node in the tree
    def sortedArrayToBST(self, a):
        return self.sortedArrayToBSTHelper(a, 0, len(a) - 1)

    def sortedArrayToBSTHelper(self, a, start, end):
        if start > end: return None
        mid = (start + end) // 2
        node = TreeNode(a[mid])
        node.left = self.sortedArrayToBSTHelper(a, start, mid - 1)
        node.right = self.sortedArrayToBSTHelper(a, mid + 1, end)
        return node

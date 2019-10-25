# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return the root node in the tree
    def buildTree(self, preorder, inorder):
        return self.buildTreeHelper(inorder, 0, len(inorder) - 1, preorder, 0, len(preorder) - 1)

    def buildTreeHelper(self, inorder, ileft, iright, preorder, pleft, pright):
        if ileft > iright: return None
        root = TreeNode(preorder[pleft])
        idx = inorder.index(root.val, ileft, iright + 1)
        lenleft = idx - ileft
        root.left = self.buildTreeHelper(inorder, ileft, idx - 1, preorder, pleft + 1, pleft + lenleft)
        root.right = self.buildTreeHelper(inorder, idx + 1, iright, preorder, pleft + lenleft + 1, pright)
        return root

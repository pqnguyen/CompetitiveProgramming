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
    def buildTree(self, inorder, postorder):
        return self.buildTreeHelper(inorder, 0, len(inorder) - 1, postorder, 0, len(postorder) - 1)

    def buildTreeHelper(self, inorder, ileft, iright, postorder, pleft, pright):
        if ileft > iright: return None
        root = TreeNode(postorder[pright])
        idx = inorder.index(root.val, ileft, iright + 1)
        lenright = iright - idx
        root.left = self.buildTreeHelper(inorder, ileft, idx - 1, postorder, pleft, pright - lenright - 1)
        root.right = self.buildTreeHelper(inorder, idx + 1, iright, postorder, pright - lenright, pright - 1)
        return root

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
        if not root: return None
        hLeft = self.getHeight(root.left)
        hRight = self.getHeight(root.right)
        if hLeft == hRight:
            return root
        elif hLeft > hRight:
            return self.lcaDeepestLeaves(root.left)
        else:
            return self.lcaDeepestLeaves(root.right)

    def getHeight(self, root):
        if not root: return 0
        return max(self.getHeight(root.left), self.getHeight(root.right)) + 1

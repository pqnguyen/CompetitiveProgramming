# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Ref:
    def __init__(self):
        self.val = None


class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        ref = Ref()
        self.flattenHelper(root, ref)
        return root

    def flattenHelper(self, root, ref):
        if not root: return None
        ref.val = root
        right = root.right
        root.right = self.flattenHelper(root.left, ref)
        root.left = None
        ref.val.right = right
        self.flattenHelper(right, ref)
        return root

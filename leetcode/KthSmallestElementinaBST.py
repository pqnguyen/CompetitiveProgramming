# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.nSmaller = 0
        return self.findKthSmallest(root, k)

    def findKthSmallest(self, root, k):
        if not root: return None
        left = self.findKthSmallest(root.left, k)
        if not left is None: return left

        self.nSmaller += 1
        if self.nSmaller == k: return root.val

        return self.findKthSmallest(root.right, k)

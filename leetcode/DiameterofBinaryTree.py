# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class RefVariable:
    def __init__(self):
        self.val = 1


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        longest = RefVariable()
        self.helper(root, longest)
        return longest.val - 1

    def helper(self, root, longest):
        if not root: return 0
        left = self.helper(root.left, longest)
        right = self.helper(root.right, longest)
        longest.val = max(longest.val, left, right, left + 1 + right)
        return max(1 + left, 1 + right)

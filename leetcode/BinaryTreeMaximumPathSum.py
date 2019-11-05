# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

MIN_INT = -2 ** 31


class MaxValue:
    def __init__(self):
        self.value = MIN_INT


class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        maxValue = MaxValue()
        self.helper(root, maxValue)
        return maxValue.value

    def helper(self, root, maxValue):
        if not root: return MIN_INT
        left = self.helper(root.left, maxValue)
        right = self.helper(root.right, maxValue)
        total = max(root.val, root.val + left, root.val + right)

        maxValue.value = max(maxValue.value, total, left, right, root.val + left + right)
        return total

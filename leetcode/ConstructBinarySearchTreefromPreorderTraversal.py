# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        root = self.bstFromPreorderUtil(preorder, 0, len(preorder) - 1)
        return root

    def bstFromPreorderUtil(self, preorder, left, right):
        if left > right: return None
        root = TreeNode(preorder[left])
        index = left + 1
        while index < len(preorder) and preorder[index] < root.val: index += 1
        root.left = self.bstFromPreorderUtil(preorder, left + 1, index - 1)
        root.right = self.bstFromPreorderUtil(preorder, index, right)
        return root

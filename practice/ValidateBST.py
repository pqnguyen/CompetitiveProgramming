# Cracking the coding interview - 4.5
# Check Balanced: Implement a function to check if a binary tree is balanced.
# For the purposes of this question, a balanced tree is defined to be a tree such
# that the heights of the two subtrees of any node never differ by more than one.


from enum import Enum


class TreeNode:
    def __init__(self, val):
        self.value = val
        self.left = self.right = None


class Solution:
    def solve(self, a):
        root = self.create_minimal_BST(a, 0, len(a) - 1)
        is_bst = self.validate_BST(root)
        print(is_bst)

        # modify balance
        node = self.find_node(root, 3)
        node.right = TreeNode(9)
        is_bst = self.validate_BST(root)
        print(is_bst)

    def validate_BST(self, root, min=None, max=None):
        if not root: return True
        if (min and min > root.value) or (max and max <= root.value):
            return False

        if not self.validate_BST(root.left, min, root.value) or not self.validate_BST(root.right, root.value, max):
            return False
        return True

    def create_minimal_BST(self, a, start, end):
        if start > end: return None
        mid = (start + end) // 2
        root = TreeNode(a[mid])
        root.left = self.create_minimal_BST(a, start, mid - 1)
        root.right = self.create_minimal_BST(a, mid + 1, end)
        return root

    def find_node(self, root, value):
        if not root: return None
        if root.value == value: return root
        if value > root.value:
            return self.find_node(root.right, value)
        else:
            return self.find_node(root.left, value)


Solution().solve([1, 2, 3, 4, 5, 6, 7, 8])

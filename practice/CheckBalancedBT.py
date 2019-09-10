# Cracking the coding interview - 4.4
# Check Balanced: Implement a function to check if a binary tree is balanced.
# For the purposes of this question, a balanced tree is defined to be a tree such
# that the heights of the two subtrees of any node never differ by more than one.


from collections import defaultdict, deque


class TreeNode:
    def __init__(self, val):
        self.value = val
        self.left = self.right = None


class Solution:
    def solve(self, a):
        root = self.create_minimal_BST(a, 0, len(a) - 1)
        is_balanced, height = self.is_balanced(root)
        print(is_balanced)

        # modify balance
        node = self.find_node(root, 8)
        node.right = TreeNode(9)
        node = self.find_node(root, 1)
        node.left = TreeNode(0)
        is_balanced, height = self.is_balanced(root)
        print(is_balanced)

    def is_balanced(self, root):
        if not root: return True, 0
        left_balanced, left_height = self.is_balanced(root.left)
        if not left_balanced: return False, 0
        right_balanced, right_height = self.is_balanced(root.right)
        if not right_balanced: return False, 0

        current_height = max(left_height, right_height) + 1
        if abs(left_height - right_height) > 1: return False, current_height
        return True, current_height

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

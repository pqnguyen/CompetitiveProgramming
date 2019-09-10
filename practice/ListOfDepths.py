# Cracking the coding interview - 4.3
# List of Depths: Given a binary tree, design an algorithm which creates a linked list of all
# the nodes at each depth (e.g., if you have a tree with depth D, you'll have Dlinked lists).


from collections import defaultdict, deque


class TreeNode:
    def __init__(self, val):
        self.value = val
        self.left = self.right = None


class Solution:
    def solve(self, a):
        root = self.create_minimal_BST(a, 0, len(a) - 1)
        ls = self.list_of_depths(root)
        print(ls)

    def list_of_depths(self, root):
        ls = []
        if not root: return ls
        current = [root]
        while current:
            ls.append([node.value for node in current])
            parents = current
            current = []
            for node in parents:
                if node.left:
                    current.append(node.left)
                if node.right:
                    current.append(node.right)
        return ls

    def create_minimal_BST(self, a, start, end):
        if start > end: return None
        mid = (start + end) // 2
        root = TreeNode(a[mid])
        root.left = self.create_minimal_BST(a, start, mid - 1)
        root.right = self.create_minimal_BST(a, mid + 1, end)
        return root


Solution().solve([1, 2, 3, 4, 5, 6, 7, 8])

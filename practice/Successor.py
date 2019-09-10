# Cracking the coding interview - 4.6
# Successor: Write an algorithm to find the "next" node (i.e., in-order successor)
# of a given node in a binary search tree. You may assume that each node has a link to its parent.

class TreeNode:
    def __init__(self, val):
        self.value = val
        self.left = self.right = None


class Solution:
    def solve(self, node):
        if not node: return None
        if node.right:
            return self.left_most(node.right)

        current = node
        parent = current.parent
        # Go up until we are on left instead of right
        while parent and parent.left != current:
            current = parent
            parent = current.parent

        return parent

    def left_most(self, node):
        if not node: return None
        while node.left:
            node = node.left
        return node

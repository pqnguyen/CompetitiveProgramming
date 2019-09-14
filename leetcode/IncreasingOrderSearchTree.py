# https://leetcode.com/problems/increasing-order-search-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        order = []
        self.inorder(root, order)
        if not order: return None
        for i in range(len(order) - 1):
            order[i].left = None
            order[i].right = order[i + 1]
            order[i + 1].left = order[i + 1].right = None
        return order[0]

    def inorder(self, root, order):
        if not root: return
        self.inorder(root.left, order)
        order.append(root)
        self.inorder(root.right, order)
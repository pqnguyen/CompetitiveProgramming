# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return an integer
    def t2Sum(self, root, target):
        if self.t2SumHelper(root, target, {}):
            return 1
        return 0

    def t2SumHelper(self, root, target, tb):
        if not root: return False
        if target - root.val in tb:
            return True
        tb[root.val] = True
        return self.t2SumHelper(root.left, target, tb) or self.t2SumHelper(root.right, target, tb)

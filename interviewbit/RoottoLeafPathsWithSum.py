# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return an integer
    def hasPathSum(self, A, B):
        res = []
        self.hasPathSumHelper(A, 0, [], B, res)
        return res

    def hasPathSumHelper(self, node, sum, path, target, res):
        if not node: return
        path.append(node.val)
        if not node.left and not node.right and sum + node.val == target:
            res.append(path[:])
        self.hasPathSumHelper(node.left, sum + node.val, path, target, res)
        self.hasPathSumHelper(node.right, sum + node.val, path, target, res)
        path.pop()

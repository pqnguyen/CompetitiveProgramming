# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @param C : integer
    # @return an integer
    def lca(self, A, B, C):
        if not A: return -1
        pathB, pathC = [], []
        if not self.findNode(A, B, pathB) or not self.findNode(A, C, pathC): return -1
        i = 0
        while i < len(pathB) and i < len(pathC) and pathB[i] == pathC[i]:
            i += 1
        return pathB[i - 1].val

    def findNode(self, node, val, path):
        if not node: return False
        path.append(node)
        if node.val == val: return True
        if self.findNode(node.left, val, path): return True
        if self.findNode(node.right, val, path): return True
        path.pop()
        return False
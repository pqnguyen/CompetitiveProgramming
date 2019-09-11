# https://leetcode.com/problems/binary-tree-paths/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        res = []
        self.dfs(root, [], res)
        return res

    def dfs(self, root, path, res):
        if not root: return
        path.append(str(root.val))
        if not root.left and not root.right:
            res.append('->'.join(path))
        if root.left:
            self.dfs(root.left, path, res)
        if root.right:
            self.dfs(root.right, path, res)
        path.pop()

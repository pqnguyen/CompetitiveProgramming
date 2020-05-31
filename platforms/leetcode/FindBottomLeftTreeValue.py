# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        visited = {}
        self.findBottomLeftValueUtil(root, 1, visited)
        level = sorted(visited)[-1]
        return visited[level]

    def findBottomLeftValueUtil(self, root, level, visited):
        if not root: return
        self.findBottomLeftValueUtil(root.left, level + 1, visited)
        if level not in visited:
            visited[level] = root.val
        self.findBottomLeftValueUtil(root.right, level + 1, visited)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        to_delete = set(to_delete)
        roots = []
        if root and root.val not in to_delete: roots.append(root)
        self.delNodesUtil(root, set(to_delete), roots)
        return roots

    def delNodesUtil(self, root, to_delete, roots):
        if not root: return None
        needDelete = root.val in to_delete
        root.left = self.delNodesUtil(root.left, to_delete, roots)
        root.right = self.delNodesUtil(root.right, to_delete, roots)
        if needDelete:
            if root.left: roots.append(root.left)
            if root.right: roots.append(root.right)
            root.left = root.right = None
            return None
        return root

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from typing import List


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        res = []
        self.helper(root, [], sum, res)
        return res

    def helper(self, root, path, sum, res):
        if not root: return
        if root.val == sum and not root.left and not root.right:
            res.append(path[:])

        path.append(root.val)
        self.helper(root.left, path, sum - root.val, res)
        self.helper(root.right, path, sum - root.val, res)
        path.pop()

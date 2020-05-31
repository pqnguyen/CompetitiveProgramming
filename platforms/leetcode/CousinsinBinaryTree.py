# https://leetcode.com/problems/cousins-in-binary-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque, defaultdict


class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        cousins = set([x, y])
        parents = deque([root])
        while parents:
            children = deque()
            m = defaultdict(int)
            while parents:
                top = parents.popleft()
                if top.left:
                    if top.left.val in cousins: m[top.left.val] = top.val
                    children.append(top.left)
                if top.right:
                    if top.right.val in cousins: m[top.right.val] = top.val
                    children.append(top.right)
            parents = children
            if m.keys():
                if m[x] and m[y] and m[x] != m[y]: return True
                return False
        return False

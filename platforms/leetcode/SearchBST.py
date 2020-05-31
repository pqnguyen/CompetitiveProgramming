from collections import deque
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        queue = deque([root])
        while queue:
            top = queue.popleft()
            if not top: continue
            if top.val == val:
                return top
            queue.append(top.left)
            queue.append(top.right)
        return None

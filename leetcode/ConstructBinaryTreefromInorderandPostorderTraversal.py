# https://leetcode.com/explore/learn/card/data-structure-tree/133/conclusion/942/
# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        n = len(inorder)
        return self.buildTreeUtil(inorder, postorder, 0, n - 1, 0, n - 1)

    def buildTreeUtil(self, inorder, postorder, istart, iend, pstart, pend):
        if istart > iend: return None
        root = TreeNode(postorder[pend])
        indexroot = self.index(inorder, istart, iend + 1, root.val)
        LSS = indexroot - istart
        RSS = iend - indexroot
        root.left = self.buildTreeUtil(inorder, postorder, istart, indexroot - 1, pstart, pstart + LSS - 1)
        root.right = self.buildTreeUtil(inorder, postorder, indexroot + 1, iend, pend - RSS, pend - 1)
        return root

    def index(self, a, start, end, val):
        for i in range(start, end):
            if a[i] == val: return i
        return -1


def traversal(root):
    if not root: return
    traversal(root.left)
    print(root.val)
    traversal(root.right)


inorder = [9, 3, 15, 20, 7]
postorder = [9, 15, 7, 20, 3]
root = Solution().buildTree(inorder, postorder)
traversal(root)

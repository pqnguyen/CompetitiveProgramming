# https://leetcode.com/explore/learn/card/data-structure-tree/17/solve-problems-recursively/536/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root: return True
        parents = [root]
        while parents:
            if not self.isArraySymmetric(parents): return False
            children = []
            for parent in parents:
                if parent:
                    children.append(parent.left)
                    children.append(parent.right)
            parents = children
        return True

    def isArraySymmetric(self, a):
        i, j = 0, len(a) - 1
        while i < j:
            if not (a[i] == a[j] == None or (a[i] and a[j] and a[i].val == a[j].val)): return False
            i += 1
            j -= 1
        return True

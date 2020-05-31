# https://leetcode.com/problems/leaf-similar-trees/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        leaves1 = self.getLeaf(root1)
        leaves2 = self.getLeaf(root2)

        if len(leaves1) != len(leaves2):
            return False

        return all(leaves1[i] == leaves2[i] for i in range(len(leaves1)))

    def getLeaf(self, root1):
        stack = [root1]
        leaves = []
        while stack:
            top = stack.pop()
            if not top.left and not top.right:
                leaves.append(top.val)

            if top.right:
                stack.append(top.right)

            if top.left:
                stack.append(top.left)

        return leaves

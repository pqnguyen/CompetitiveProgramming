# Definition for a  binary tree node
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree node
    # @return nothing
    def connect(self, root):
        if not root: return None
        parents = [root]
        while parents:
            for i in range(len(parents) - 1):
                parents[i].next = parents[i + 1]

            children = []
            for parent in parents:
                if parent.left:
                    children.append(parent.left)
                if parent.right:
                    children.append(parent.right)
            parents = children
        return root

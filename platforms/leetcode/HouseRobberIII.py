# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class RefVariable:
    def __init__(self):
        self.val = 0


class Solution:
    def __init__(self):
        self.memo = {None: 0}

    def rob(self, root: TreeNode) -> int:
        self.memo = {None: 0}
        self.maximalRob(root)
        return max(self.memo.values())

    def maximalRob(self, root):
        if not root: return
        self.maximalRob(root.left)
        self.maximalRob(root.right)
        self.memo[root] = max(root.val + self.next(root, 0, 2) + self.next(root, 1, 2),
                              self.next(root, 0, 1) + self.next(root, 1, 1))

    def next(self, root, isLeft, step):
        if isLeft:
            root = root.left
        else:
            root = root.right
        if root and step > 1: return self.memo[root.left] + self.memo[root.right]
        return self.memo[root]


root = TreeNode(3)
root.left = TreeNode(2)
root.left.right = TreeNode(3)
root.right = TreeNode(3)
root.right.right = TreeNode(1)
res = Solution().rob(root)
print(res)

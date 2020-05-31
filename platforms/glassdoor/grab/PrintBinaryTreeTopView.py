class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def top_side_view(self, root):
        res = {}
        self.dfs(root, res)
        return [res[key] for key in sorted(res.keys())]

    def dfs(self, root, res, level=1, hd=0, dict={}):
        if root is None:
            return

        if hd not in dict:
            dict[hd] = level
            res[hd] = root.val
        elif dict[hd] > level:
            dict[hd] = level
            res[hd] = root.val

        self.dfs(root.left, res, level + 1, hd - 1, dict)
        self.dfs(root.right, res, level + 1, hd + 1, dict)


a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
d = TreeNode(4)
e = TreeNode(5)
f = TreeNode(6)
g = TreeNode(7)
a.left = b
a.right = c
b.right = d
c.right = e
d.left = f
f.left = g

sol = Solution()
res = sol.top_side_view(a)
print(res)

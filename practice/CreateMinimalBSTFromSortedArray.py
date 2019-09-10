# Cracking the coding interview - 4.2
# Minimal Tree: Given a sorted (increasing order) array with unique integer elements,
# write an algorithm to create a binary search tree with minimal height.


from collections import defaultdict, deque


class TreeNode:
    def __init__(self, val):
        self.value = val
        self.left = self.right = None


class Solution:
    def solve(self, a):
        root = self.create_minimal_BST(a, 0, len(a) - 1)
        self.bfs(root)

    def traversal(self, root):
        if not root: return
        self.traversal(root.left)
        print(root.value)
        self.traversal(root.right)

    def bfs(self, root):
        q = deque()
        q.append(root)
        while q:
            current = q.popleft()
            if not current: continue
            print(current.value)
            q.append(current.left)
            q.append(current.right)

    def create_minimal_BST(self, a, start, end):
        if start > end: return None
        mid = (start + end) // 2
        root = TreeNode(a[mid])
        root.left = self.create_minimal_BST(a, start, mid - 1)
        root.right = self.create_minimal_BST(a, mid + 1, end)
        return root


Solution().solve([1, 2, 3, 4, 5, 6, 7, 8])

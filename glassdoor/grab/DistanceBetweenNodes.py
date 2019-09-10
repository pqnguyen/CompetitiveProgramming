from collections import defaultdict

MAX = 1e6


###
# 1st approach: dfs/bfs
# - convert tree into graph, using dfs/bfs find distance between two nodes
###

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class FirstApproach:
    def solve(self, root, a, b):
        graph = self.convert_to_graph(root)
        distance = self.dfs(graph, a, b, set())
        return distance

    def dfs(self, graph, source, target, visited):
        visited.add(source)
        if source == target:
            return 0

        for neighbor in graph[source]:
            if neighbor in visited:
                continue
            d = self.dfs(graph, neighbor, target, visited)
            if d != MAX:
                return 1 + d

        return MAX

    def convert_to_graph(self, root):
        graph = defaultdict(list)
        queue = [root]
        while queue:
            top = queue.pop()
            if top.left:
                graph[top.val].append(top.left.val)
                graph[top.left.val].append(top.val)
                queue.append(top.left)

            if top.right:
                graph[top.val].append(top.right.val)
                graph[top.right.val].append(top.val)
                queue.append(top.right)

        return graph


###
# 2nd approach: dfs/bfs
# - find the lowest common ancestor
# - sum up depths from LCA to a and LCA to b
###

class SecondApproach:
    def solve(self, root, a, b):
        lca = self.LCA(root, a, b)
        return self.bfs(lca, a) + self.bfs(lca, b)

    def LCA(self, root, a, b):
        if root is None or root.val == a or root.val == b:
            return root

        left = self.LCA(root.left, a, b)
        right = self.LCA(root.right, a, b)
        if left and right:
            return root

        return left if left else right

    def bfs(self, parent, child):
        q = [(parent, 0)]
        while q:
            top, d = q.pop()
            if top.val == child:
                return d

            if top.left:
                q.append((top.left, d + 1))

            if top.right:
                q.append((top.right, d + 1))

        return MAX


"""
            1
          /   \
        2       3
      /   \       \
    4      5        6
          / \
         7   8
              \
               9
"""
a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
d = TreeNode(4)
e = TreeNode(5)
f = TreeNode(6)
g = TreeNode(7)
h = TreeNode(8)
i = TreeNode(9)
a.left = b
a.right = c
b.left = d
b.right = e
c.right = f
e.left = g
e.right = h
h.right = i

# sol = FirstApproach()
sol = SecondApproach()
# 2
print(sol.solve(a, 3, 2))
# 2
print(sol.solve(a, 1, 4))
# 3
print(sol.solve(a, 7, 9))
# 4
print(sol.solve(a, 3, 8))

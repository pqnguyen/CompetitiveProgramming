from typing import List


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        colors = [0] * len(graph)
        visited = set()
        for root in range(len(graph)):
            if root not in visited:
                if not self.dfs(graph, root, visited, colors, 0): return False
        return True

    def dfs(self, graph, root, visited, colors, color):
        visited.add(root)
        colors[root] = color
        for neighbor in graph[root]:
            if neighbor not in visited:
                if not self.dfs(graph, neighbor, visited, colors, 1 - color): return False
            elif colors[neighbor] == color:
                return False
        return True


res = Solution().isBipartite(
    [[], [2, 4, 6], [1, 4, 8, 9], [7, 8], [1, 2, 8, 9], [6, 9], [1, 5, 7, 8, 9], [3, 6, 9], [2, 3, 4, 6, 9],
     [2, 4, 5, 6, 7, 8]])
print(res)

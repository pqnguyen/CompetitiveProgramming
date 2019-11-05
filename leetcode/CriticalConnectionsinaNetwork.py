from collections import defaultdict
from typing import List


class Solution:
    def __init__(self):
        self.time = 0

    def getTime(self):
        self.time += 1
        return self.time

    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(set)
        for u, v in connections:
            graph[u].add(v)
            graph[v].add(u)
        disc = [0] * n
        low = [0] * n
        parents = [-1] * n
        res = []
        for root in range(n):
            if not disc[root]: self.tarjar(graph, disc, low, root, parents, res)

        return res

    def tarjar(self, graph, disc, low, root, parents, res):
        disc[root] = low[root] = self.getTime()
        for neighbor in graph[root]:
            if not disc[neighbor]:
                parents[neighbor] = root
                self.tarjar(graph, disc, low, neighbor, parents, res)
                low[root] = min(low[root], low[neighbor])

                if disc[root] < low[neighbor]:
                    res.append([root, neighbor])
            elif neighbor != parents[root]:
                low[root] = min(low[root], disc[neighbor])


n = 4
connections = [[0, 1], [1, 2], [2, 0], [1, 3]]
res = Solution().criticalConnections(n, connections)
print(res)

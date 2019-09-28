from collections import defaultdict
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for pair in prerequisites: graph[pair[0]].append(pair[1])
        visited = [False] * numCourses
        for root in range(numCourses):
            if not visited[root]:
                if self.isCirclic(graph, root, set(), visited): return False
        return True

    def isCirclic(self, graph, root, paths, visited):
        visited[root] = True
        paths.add(root)
        for neighbor in graph[root]:
            if not visited[neighbor]:
                if self.isCirclic(graph, neighbor, paths, visited): return True
            elif neighbor in paths:
                return True
        paths.remove(root)
        return False


res = Solution().canFinish(2, [[1, 0]])
print(res)

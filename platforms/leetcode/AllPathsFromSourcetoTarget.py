from typing import List


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        res = []
        N = len(graph) - 1
        self.allPathsSourceTargetUtil(graph, 0, N, [0], res)
        return res

    def allPathsSourceTargetUtil(self, graph, start, dest, path, res):
        if start == dest:
            res.append(path[:])
            return

        for neighbor in graph[start]:
            path.append(neighbor)
            self.allPathsSourceTargetUtil(graph, neighbor, dest, path, res)
            path.pop()


graph = [[1, 2], [3], [3], []]
res = Solution().allPathsSourceTarget(graph)
print(res)

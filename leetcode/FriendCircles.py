from collections import defaultdict
from typing import List


class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        n = len(M)
        visited = defaultdict(bool)
        circleN = 0
        for student in range(n):
            if not visited[student]:
                self.dfs(M, n, student, visited)
                circleN += 1
        return circleN

    def dfs(self, M, n, start, visited):
        visited[start] = True
        for student in range(n):
            if not visited[student] and M[start][student]:
                self.dfs(M, n, student, visited)


M = [[1, 1, 0],
     [1, 1, 1],
     [0, 1, 1]]
res = Solution().findCircleNum(M)
print(res)

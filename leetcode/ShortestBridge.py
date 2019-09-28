from collections import deque
from typing import List


class Solution:
    def shortestBridge(self, A: List[List[int]]) -> int:
        m, n = len(A), len(A[0])
        queue = self.helper(A, m, n)
        visited = set()
        while queue:
            row, col, d = queue.popleft()
            for nrow, ncol in self.neighbors(m, n, row, col):
                if A[nrow][ncol] == 0 and (nrow, ncol) not in visited:
                    queue.append((nrow, ncol, d + 1))
                    visited.add((nrow, ncol))
                elif A[nrow][ncol] == 1:
                    return d
        return 0

    def helper(self, A, m, n):
        queue = deque()
        for i in range(m):
            for j in range(n):
                if A[i][j] == 1:
                    self.dfs(A, m, n, i, j, queue)
                    return queue
        return queue

    def dfs(self, A, m, n, row, col, queue):
        A[row][col] = 2
        for nrow, ncol in self.neighbors(m, n, row, col):
            if A[nrow][ncol] == 0:
                queue.append((row, col, 0))
                break

        for nrow, ncol in self.neighbors(m, n, row, col):
            if A[nrow][ncol] == 1: self.dfs(A, m, n, nrow, ncol, queue)

    def neighbors(self, m, n, row, col):
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nrow = dr + row
            ncol = dc + col
            if 0 <= nrow < m and 0 <= ncol < n:
                yield nrow, ncol


a = [[1, 1, 1, 1, 1], [1, 0, 0, 0, 1], [1, 0, 1, 0, 1], [1, 0, 0, 0, 1], [1, 1, 1, 1, 1]]
res = Solution().shortestBridge(a)
print(res)

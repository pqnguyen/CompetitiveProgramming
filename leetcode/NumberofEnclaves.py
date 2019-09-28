from typing import List


class Solution:
    def numEnclaves(self, A: List[List[int]]) -> int:
        if not A: return 0
        m, n = len(A), len(A[0])
        for i in range(m):
            if A[i][0] == 1: self.dfs(A, m, n, i, 0)
            if A[i][n - 1] == 1: self.dfs(A, m, n, i, n - 1)

        for j in range(n):
            if A[0][j] == 1: self.dfs(A, m, n, 0, j)
            if A[m - 1][j] == 1: self.dfs(A, m, n, m - 1, j)
        res = 0
        for i in range(1, m):
            for j in range(1, n):
                if A[i][j] == 1: res += 1
        return res

    def dfs(self, A, m, n, row, col):
        A[row][col] = 0
        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nrow = di + row
            ncol = dj + col
            if 0 <= nrow < m and 0 <= ncol < n and A[nrow][ncol] == 1:
                self.dfs(A, m, n, nrow, ncol)


res = Solution().numEnclaves([[0, 1, 1, 0], [0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 0, 0]])
print(res)

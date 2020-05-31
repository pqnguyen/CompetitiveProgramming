from typing import List


class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        max_row = [-1] * n
        max_col = [-1] * m
        for i in range(n):
            for j in range(m):
                max_col[j] = max(max_col[j], grid[i][j])
                max_row[i] = max(max_row[i], grid[i][j])

        res = 0
        for i in range(n):
            for j in range(m):
                res += (min(max_row[i], max_col[j]) - grid[i][j])
        return res


grid = [[3, 0, 8, 4], [2, 4, 5, 7], [9, 2, 6, 3], [0, 3, 1, 0]]
res = Solution().maxIncreaseKeepingSkyline(grid)
print(res)

# https://leetcode.com/problems/rotting-oranges/
from collections import deque
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        n, m = len(grid), len(grid[0])
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    queue.append((i, j, 0))

        def neighbors(i, j):
            for ir, ic in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = i + ir, j + ic
                if 0 <= nr < n and 0 <= nc < m:
                    yield nr, nc

        d = 0
        while queue:
            r, c, d = queue.popleft()
            for nr, nc in neighbors(r, c):
                if grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    queue.append((nr, nc, d + 1))

        if any(1 in row for row in grid):
            return -1
        return d
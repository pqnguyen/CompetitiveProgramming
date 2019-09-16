# https://leetcode.com/explore/learn/card/queue-stack/231/practical-application-queue/1374/

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: return 0
        n, m = len(grid), len(grid[0])
        nIslands = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1':
                    self.bfs(grid, n, m, i, j)
                    nIslands += 1
        return nIslands

    def bfs(self, grid, n, m, i, j):
        def neighbors(i, j):
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                r, c = i + dr, j + dc
                if 0 <= r < n and 0 <= c < m:
                    yield (r, c)

        queue = collections.deque()
        queue.append((i, j))
        grid[i][j] = '-1'
        while queue:
            i, j = queue.popleft()
            for r, c in neighbors(i, j):
                if grid[r][c] == '1':
                    queue.append((r, c))
                    grid[r][c] = '-1'

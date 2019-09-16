# https://leetcode.com/explore/learn/card/queue-stack/239/conclusion/1388/
import collections
from typing import List


class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix: return matrix
        n, m = len(matrix), len(matrix[0])
        d = [[0] * m for _ in range(n)]
        queue = collections.deque()
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    queue.append((i, j))

        while queue:
            sr, sc = queue.popleft()
            for r, c in self.neighbors(n, m, sr, sc):
                if matrix[r][c] == 1 and not d[r][c]:
                    d[r][c] = d[sr][sc] + 1
                    queue.append((r, c))

        return d

    def neighbors(self, n, m, sr, sc):
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            r, c = dr + sr, dc + sc
            if 0 <= r < n and 0 <= c < m:
                yield (r, c)


res = Solution().updateMatrix(
    [[0, 0, 1, 0, 1, 1, 1, 0, 1, 1], [1, 1, 1, 1, 0, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 0, 0, 0, 1, 1],
     [1, 0, 1, 0, 1, 1, 1, 0, 1, 1], [0, 0, 1, 1, 1, 0, 1, 1, 1, 1], [1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
     [1, 1, 1, 1, 0, 1, 0, 1, 0, 1], [0, 1, 0, 0, 0, 1, 0, 0, 1, 1], [1, 1, 1, 0, 1, 1, 0, 1, 0, 1],
     [1, 0, 1, 1, 1, 0, 1, 1, 1, 0]])
print(res)

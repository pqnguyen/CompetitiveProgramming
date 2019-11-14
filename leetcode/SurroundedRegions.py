from collections import deque
from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board: return
        m, n = len(board), len(board[0])
        visited = set()
        queue = deque()
        for i in range(n):
            if board[0][i] == 'O': queue.append((0, i))
            if board[m - 1][i] == 'O': queue.append((m - 1, i))

        for i in range(m):
            if board[i][0] == 'O': queue.append((i, 0))
            if board[i][n - 1] == 'O': queue.append((i, n - 1))

        for r, c in queue: visited.add((r, c))

        while queue:
            row, col = queue.popleft()

            for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                r = dr + row
                c = dc + col
                if 0 <= r < m and 0 <= c < n:
                    if board[r][c] == 'O' and (r, c) not in visited:
                        queue.append((r, c))
                        visited.add((r, c))

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O' and (i, j) not in visited:
                    board[i][j] = 'X'


board = [["X", "X", "X", "X"], ["X", "O", "O", "X"], ["X", "X", "O", "X"], ["X", "O", "X", "X"]]
Solution().solve(board)
print(board)

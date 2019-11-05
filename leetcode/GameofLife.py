from typing import List


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                cnt = self.countStateNeighbors(board, m, n, i, j, {1, 3})
                if board[i][j] == 0:
                    if cnt == 3: board[i][j] = 2
                else:
                    if cnt < 2 or cnt > 3: board[i][j] = 3
        for i in range(m):
            for j in range(n):
                if board[i][j] == 2:
                    board[i][j] = 1
                elif board[i][j] == 3:
                    board[i][j] = 0

    def countStateNeighbors(self, board, m, n, row, col, state):
        def neighbors(r, c):
            for dr, dc in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
                row = dr + r
                col = dc + c
                if self.isValid(m, n, row, col):
                    yield (row, col)

        count = 0
        for r, c in neighbors(row, col):
            if board[r][c] in state: count += 1
        return count

    def isValid(self, m, n, row, col):
        return 0 <= row < m and 0 <= col < n


board = [
    [0, 1, 0],
    [0, 0, 1],
    [1, 1, 1],
    [0, 0, 0]
]
Solution().gameOfLife(board)
for row in board: print(row)

from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])

        def neighbors(r, c, target):
            for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                row = r + dr
                col = c + dc
                if 0 <= row < m and 0 <= col < n and board[row][col] == target:
                    yield (row, col)

        def dfs(r, c, path, i):
            if i + 1 == len(word): return True
            path.add((r, c))
            for row, col in neighbors(r, c, word[i + 1]):
                if (row, col) not in path:
                    if dfs(row, col, path, i + 1): return True
            path.remove((r, c))
            return False

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if dfs(i, j, set(), 0): return True

        return False


board = [["b", "a", "a", "b", "a", "b"],
         ["a", "b", "a", "a", "a", "a"],
         ["a", "b", "a", "a", "a", "b"],
         ["a", "b", "a", "b", "b", "a"],
         ["a", "a", "b", "b", "a", "b"],
         ["a", "a", "b", "b", "b", "a"],
         ["a", "a", "b", "a", "a", "b"]]

print(Solution().exist(board, "aabbbbabbaababaaaabababbaaba"))

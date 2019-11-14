from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m, n = len(matrix), len(matrix[0])
        isFirstRowZero = any([matrix[0][i] == 0 for i in range(n)])
        isFirstColZero = any([matrix[i][0] == 0 for i in range(m)])

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[0][i] = 0
                    matrix[i][0] = 0
        for i in range(1, n):
            if matrix[0][i] == 0: self.setZero(matrix, m, n, 0, i, 1, 0)

        for i in range(1, m):
            if matrix[i][0] == 0: self.setZero(matrix, m, n, i, 0, 0, 1)

        if isFirstColZero: self.setZero(matrix, m, n, 0, 0, 1, 0)
        if isFirstRowZero: self.setZero(matrix, m, n, 0, 0, 0, 1)

    def setZero(self, matrix, m, n, row, col, dr, dc):
        while 0 <= row < m and 0 <= col < n:
            matrix[row][col] = 0
            row = row + dr
            col = col + dc


matrix = [
    [0, 1, 2, 0],
    [3, 4, 5, 2],
    [1, 3, 1, 5]
]
Solution().setZeroes(matrix)
for row in matrix: print(row)

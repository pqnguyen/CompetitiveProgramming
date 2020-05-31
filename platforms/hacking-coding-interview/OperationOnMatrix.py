class Solution:
    def snake_matrix(self, matrix):
        res = []
        if not matrix: return res
        n, m = len(matrix), len(matrix[0])
        for i in range(n):
            for j in range(m):
                col = m - j - 1 if i % 2 else j
                res.append(matrix[i][col])

        return res


a = [
    [1, 2, 3, 4, 5],
    [10, 9, 8, 7, 6],
    [11, 12, 13, 14, 15],
    [20, 19, 18, 17, 16]
]
res = Solution().snake_matrix(a)
print(res)


class SolutionII:
    def zigzag_matrix(self, matrix):
        res = []
        if not matrix: return res
        n, m = len(matrix), len(matrix[0])
        even = True
        for r in range(n):
            row, col = r, 0
            tmp = []
            while 0 <= row < n and 0 <= col < m:
                tmp.append(matrix[row][col])
                row -= 1
                col += 1
            res.extend(tmp if even else reversed(tmp))
            even = not even

        for c in range(1, m):
            row, col = n - 1, c
            tmp = []
            while 0 <= row < n and 0 <= col < m:
                tmp.append(matrix[row][col])
                row -= 1
                col += 1
            res.extend(tmp if even else reversed(tmp))
            even = not even

        return res


res = SolutionII().zigzag_matrix(a)
print(res)

# https://leetcode.com/problems/spiral-matrix/
from typing import List


class SolutionIII:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not len(matrix): return
        n, m = len(matrix), len(matrix[0])
        res = []
        top, bottom = 0, n - 1
        left, right = 0, m - 1
        while True:
            if left > right: break
            for i in range(left, right + 1):
                res.append(matrix[top][i])
            top += 1

            if top > bottom: break
            for i in range(top, bottom + 1):
                res.append(matrix[i][right])
            right -= 1

            if left > right: break
            for i in range(right, left - 1, -1):
                res.append(matrix[bottom][i])
            bottom -= 1

            if top > bottom: break
            for i in range(bottom, top - 1, -1):
                res.append(matrix[i][left])
            left += 1
        return res


# https://leetcode.com/problems/spiral-matrix-iii/


class SolutionIV:
    def spiralMatrixIII(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        ans = [[r0, c0]]
        if R * C == 1: return ans

        # For walk length k = 1, 3, 5 ...
        for k in range(1, 2 * max(R, C), 2):

            # For direction (dr, dc) = east, south, west, north;
            # and walk length dk...
            for dr, dc, dk in ((0, 1, k), (1, 0, k), (0, -1, k + 1), (-1, 0, k + 1)):

                # For each of dk units in the current direction ...
                for _ in range(dk):

                    # Step in that direction
                    r0 += dr
                    c0 += dc

                    # If on the grid ...
                    if 0 <= r0 < R and 0 <= c0 < C:
                        ans.append([r0, c0])
                        if len(ans) == R * C:
                            return ans

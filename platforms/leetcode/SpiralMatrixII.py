# https://leetcode.com/problems/spiral-matrix-ii/
from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0] * n for i in range(n)]
        top, bottom = 0, n - 1
        left, right = 0, n - 1
        count = 1
        while True:
            if left > right: break
            for i in range(left, right + 1):
                matrix[top][i] = count
                count += 1
            top += 1

            if top > bottom: break
            for i in range(top, bottom + 1):
                matrix[i][right] = count
                count += 1
            right -= 1

            if left > right: break
            for i in range(right, left - 1, -1):
                matrix[bottom][i] = count
                count += 1
            bottom -= 1

            if top > bottom: break
            for i in range(bottom, top - 1, -1):
                matrix[i][left] = count
                count += 1
            left += 1

        return matrix


matrix = Solution().generateMatrix(4)
for a in matrix:
    print(a)

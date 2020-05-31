# https://leetcode.com/problems/spiral-matrix/
from typing import List


class Solution:
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

class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix: return []
        res = []
        m, n = len(matrix), len(matrix[0])
        direction = [(-1, 1), (1, -1)]
        d = i = j = 0
        for _ in range(m * n):
            res.append(matrix[i][j])
            i += direction[d][0]
            j += direction[d][1]
            # be careful about these order, they must be the same order as below
            if i >= m:
                j += 2
                d = 1 - d
                i = m - 1
            if j >= n:
                i += 2
                d = 1 - d
                j = n - 1
            if i < 0:
                i = 0
                d = 1 - d
            if j < 0:
                j = 0
                d = 1 - d
        return res

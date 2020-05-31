class Solution:
    def matrixScore(self, A: List[List[int]]) -> int:
        n, m = len(A), len(A[0])
        for i in range(n):
            if A[i][0] == 0:
                self.switch(A, n, m, 0, i, 1, 0)

        for j in range(1, m):
            zero = 0
            for i in range(n):
                if A[i][j] == 0: zero += 1
            if zero > n - zero:
                self.switch(A, n, m, j, 0, 0, 1)

        res = 0
        for row in A:
            res += self.rowToNumber(row)
        return res

    def rowToNumber(self, row):
        res = 0
        n = len(row)
        for i in range(n):
            if row[i]: res += 2 ** (n - i - 1)
        return res

    def switch(self, A, n, m, sc, sr, c, r):
        while sc < m and sr < n:
            A[sr][sc] = 1 - A[sr][sc]
            sc += c
            sr += r

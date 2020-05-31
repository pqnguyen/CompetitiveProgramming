class Solution:
    # @param A : integer
    # @return a list of list of strings
    def solveNQueens(self, n):
        a = [['.'] * n for _ in range(n)]
        res = []
        self.solveNQueensHelper(a, n, 0, res)
        return res

    def solveNQueensHelper(self, a, n, i, res):
        if i == n:
            res.append(self.snapshot(a))
            return
        for j in range(n):
            if self.isPlaced(a, n, i, j):
                a[i][j] = 'Q'
                self.solveNQueensHelper(a, n, i + 1, res)
                a[i][j] = '.'

    def snapshot(self, a):
        res = []
        for row in a:
            res.append("".join(row))
        return res

    def isPlaced(self, a, n, row, col):
        for i in range(n):
            if a[i][col] == 'Q': return False

        i, j = row, col
        while 0 <= i < n and 0 <= j < n:
            if a[i][j] == 'Q': return False
            i -= 1
            j += 1

        i, j = row, col
        while 0 <= i < n and 0 <= j < n:
            if a[i][j] == 'Q': return False
            i -= 1
            j -= 1

        i, j = row, col
        while 0 <= i < n and 0 <= j < n:
            if a[i][j] == 'Q': return False
            i += 1
            j -= 1

        i, j = row, col
        while 0 <= i < n and 0 <= j < n:
            if a[i][j] == 'Q': return False
            i += 1
            j += 1
        return True


res = Solution().solveNQueens(4)
print(res)

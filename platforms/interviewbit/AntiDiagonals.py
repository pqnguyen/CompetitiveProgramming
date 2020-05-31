class Solution:
    # @param A : list of list of integers
    # @return a list of list of integers
    def diagonal(self, A):
        n = len(A)
        i, j = 0, 0
        res = []
        for k in range(n + n - 1):
            diag = []
            row, col = i, j
            while 0 <= row < n and 0 <= col < n:
                diag.append(A[row][col])
                row += 1
                col -= 1
            res.append(diag)

            if j < n - 1:
                j += 1
            else:
                i += 1
        return res

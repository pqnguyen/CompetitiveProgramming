class Solution:
    # @param A : list of list of integers
    # @return the same list modified
    def setZeroes(self, A):
        m, n = len(A), len(A[0])
        rows, cols = set(), set()
        for i in range(0, m):
            for j in range(0, n):
                if A[i][j] == 0:
                    rows.add(i)
                    cols.add(j)

        for i in range(0, m):
            for j in range(0, n):
                if i in rows or j in cols:
                    A[i][j] = 0

        return A


A = [[1, 0, 1],
     [1, 1, 1],
     [1, 1, 1]]
res = Solution().setZeroes(A)
print(res)

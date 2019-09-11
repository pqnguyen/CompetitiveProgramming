# https://leetcode.com/problems/transpose-matrix/
class Solution:
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        n, m = len(A), len(A[0])
        res = [[0] * n for _ in range(m)]

        for i in range(n):
            for j in range(m):
                res[j][i] = A[i][j]

        return res

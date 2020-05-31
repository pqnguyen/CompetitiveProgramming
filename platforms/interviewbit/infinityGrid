class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def coverPoints(self, A, B):
        res = 0
        for i in range(1, len(A)):
            res += max(abs(A[i] - A[i - 1]), abs(B[i] - B[i - 1]))
        return res


res = Solution().coverPoints([0, 1, 1], [0, 1, 2])
print(res)

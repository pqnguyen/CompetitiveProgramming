class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of list of integers
    def combinationSum(self, A, B):
        A = list(set(A))
        res = []
        self.combinationSumHelper(A, B, 0, [], res)
        res.sort()
        return res

    def combinationSumHelper(self, A, B, index, a, res):
        if B < 0 or index >= len(A): return
        if B == 0:
            res.append(a[:])
            return
        a.append(A[index])
        self.combinationSumHelper(A, B - A[index], index, a, res)
        a.pop()
        self.combinationSumHelper(A, B, index + 1, a, res)


A = [2, 3, 6, 7]
res = Solution().combinationSum(A, 7)
print(res)

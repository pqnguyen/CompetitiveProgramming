class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of list of integers
    def combinationSum(self, A, B):
        A.sort()
        res = []
        self.combinationSumHelper(A, B, 0, [], res, {})
        res.sort()
        return res

    def combinationSumHelper(self, A, B, index, a, res, tb):
        if B == 0:
            key = ":".join(str(num) for num in a)
            if key not in tb:
                res.append(a[:])
                tb[key] = True
            return
        if B < 0 or index >= len(A): return
        a.append(A[index])
        self.combinationSumHelper(A, B - A[index], index + 1, a, res, tb)
        a.pop()
        self.combinationSumHelper(A, B, index + 1, a, res, tb)


A = [1, 11, 16]
res = Solution().combinationSum(A, 28)
print(res)

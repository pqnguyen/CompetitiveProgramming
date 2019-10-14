class Solution:
    # @param A : integer
    # @param B : integer
    # @return a list of list of integers
    def combine(self, n, k):
        A = [i for i in range(1, n + 1)]
        res = []
        self.combineHelper(A, k, 0, [], res)
        return res

    def combineHelper(self, A, B, index, arr, res):
        if B == 0:
            res.append(arr[:])
            return
        if index >= len(A): return

        arr.append(A[index])
        self.combineHelper(A, B - 1, index + 1, arr, res)
        arr.pop()
        self.combineHelper(A, B, index + 1, arr, res)


A = [1, 2, 3, 4]
res = Solution().combine(A, 2)
print(res)

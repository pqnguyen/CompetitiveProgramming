class Solution:
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @param C : tuple of integers
    # @return an integer
    def minimize(self, A, B, C):
        res = 2 ** 31 - 1
        arrs = [A, B, C]
        idxs = [0, 0, 0]
        isContinue = True
        while isContinue:
            miindex = 0
            for i in range(3):
                if idxs[i] >= len(arrs[i]):
                    isContinue = False
                    break
                if arrs[i][idxs[i]] < arrs[miindex][idxs[miindex]]:
                    miindex = i
            if isContinue:
                i, j, k = idxs[0], idxs[1], idxs[2]
                res = min(res, max(abs(A[i] - B[j]), abs(B[j] - C[k]), abs(C[k] - A[i])))
                idxs[miindex] += 1
        return res


A = [1, 4, 10]
B = [2, 15, 20]
C = [10, 12]
res = Solution().minimize(A, B, C)
print(res)

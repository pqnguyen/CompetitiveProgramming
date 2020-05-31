class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @param C : list of integers
    # @return an integer
    def solve(self, A, B, C):
        a = [A, B, C]
        idxs = [0] * 3
        res = 2 ** 31 - 1
        isContinue = True
        while isContinue:
            miindex = 0
            for i in range(3):
                if idxs[i] >= len(a[i]):
                    isContinue = False
                    break
                if a[i][idxs[i]] < a[miindex][idxs[miindex]]:
                    miindex = i
            if isContinue:
                tmp = [a[i][idx] for i, idx in enumerate(idxs)]
                res = min(res, max(tmp) - min(tmp))
            idxs[miindex] += 1
        return res


A = [1, 4, 5, 8, 10]
B = [6, 9, 15]
C = [2, 3, 6, 6]
res = Solution().solve(A, B, C)
print(res)

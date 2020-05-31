class Solution:
    # @param A : list of integers
    # @return a list of integers
    def equal(self, A):
        tb = {}
        n = len(A)
        res = []
        for i in range(n - 1):
            for j in range(i + 1, n):
                total = A[i] + A[j]
                if total in tb:
                    ii, jj = tb[total]
                    if ii == i or ii == j or jj == i or jj == j: continue
                    tmp = [ii, jj, i, j]
                    if not res:
                        res = tmp
                    else:
                        res = min(res, tmp)
                else:
                    tb[total] = (i, j)
        return res


res = Solution().equal([1, 1, 1, 1])
print(res)

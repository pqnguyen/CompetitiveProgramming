class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def threeSum(self, A):
        A.sort()
        res = []
        for k in range(len(A) - 2):
            if k > 0 and A[k] == A[k - 1]: continue
            i, j = k + 1, len(A) - 1
            while i < j:
                total = A[k] + A[i] + A[j]
                if total == 0:
                    res.append([A[k], A[i], A[j]])
                if total > 0:
                    j -= 1
                    while j > i and A[j] == A[j + 1]: j -= 1
                else:
                    i += 1
                    while i < j and A[i] == A[i - 1]: i += 1
        return res


S = [-4, 0, 4]
res = Solution().threeSum(S)
print(res)

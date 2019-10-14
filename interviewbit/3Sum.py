class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def threeSumClosest(self, A, B):
        res = 2 ** 31 - 1
        A.sort()
        for k in range(len(A) - 2):
            i, j = k + 1, len(A) - 1
            while i < j:
                total = A[k] + A[i] + A[j]
                if total > B:
                    j -= 1
                else:
                    i += 1
                if abs(total - B) < abs(res - B):
                    res = total
        return res


S = [-1, 2, 1, -4]
res = Solution().threeSumClosest(S, 1)
print(res)

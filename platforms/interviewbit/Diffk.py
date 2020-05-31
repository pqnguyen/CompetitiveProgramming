class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def diffPossible(self, A, B):
        if len(A) < 1: return 0
        i, j = 0, 1
        while j < len(A):
            if A[j] - A[i] == B: return 1
            if A[j] - A[i] > B:
                i += 1
            else:
                j += 1
            if i >= j:
                j = i + 1
        return 0


A = [1, 1, 2, 3, 4, 5]
res = Solution().diffPossible(A, 0)
print(res)

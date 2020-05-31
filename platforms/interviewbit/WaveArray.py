class Solution:
    # @param A : list of integers
    # @return a list of integers
    def wave(self, A):
        A.sort()
        for i in range(1, len(A), 2):
            if A[i] > A[i - 1]:
                A[i], A[i - 1] = A[i - 1], A[i]
        return A


res = Solution().wave([1, 2, 3, 4, 5])
print(res)

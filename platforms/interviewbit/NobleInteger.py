class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        if not A: return -1
        A.sort()
        n = len(A)
        for i in range(n - 1, -1, -1):
            if (i == n - 1 or A[i] < A[i + 1]) and A[i] == n - i - 1:
                return 1
        return -1


res = Solution().solve([-1])
print(res)

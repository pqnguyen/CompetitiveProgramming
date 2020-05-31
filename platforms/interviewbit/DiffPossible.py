class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def diffPossible(self, A, B):
        tb = {}
        for num in A:
            if num + B in tb or num - B in tb: return 1
            tb[num] = 1
        return 0


A = [1, 2, 3]
res = Solution().diffPossible(A, 2)
print(res)

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxSubArray(self, A):
        res = current_sum = -2 ** 31
        for i in range(len(A)):
            current_sum = max(current_sum + A[i], A[i])
            res = max(res, current_sum)
        return res


res = Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
print(res)

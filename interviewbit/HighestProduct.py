class Solution:
    # @param A : list of integers
    # @return an integer
    def maxp3(self, A):
        A.sort()
        return max(A[0] * A[1] * A[-1], A[-1] * A[-2] * A[-3])


res = Solution().maxp3([0, -1, 3, 100, 70, 50])
print(res)

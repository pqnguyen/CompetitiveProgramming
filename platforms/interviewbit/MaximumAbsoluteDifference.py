class Solution:
    # @param A : list of integers
    # @return an integer
    def maxArr(self, A):
        mxSum = mxSub = -2 ** 32
        miSum = miSub = 2 ** 31 - 1
        for ai, i in enumerate(A):
            mxSum = max(mxSum, ai + i)
            mxSub = max(mxSub, ai - i)
            miSum = min(miSum, ai + i)
            miSub = min(miSub, ai - i)
        return max(mxSum - miSum, mxSub - miSub)


res = Solution().maxArr([1, 3, -1])
print(res)

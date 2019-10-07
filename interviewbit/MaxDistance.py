class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maximumGap(self, A):
        a = [(ele, i) for i, ele in enumerate(A)]
        a.sort()
        res = 0
        smallestIndex = 2 ** 31 - 1
        for i in range(len(a)):
            ele, index = a[i]
            res = max(res, index - smallestIndex)
            smallestIndex = min(smallestIndex, index)
        return res


res = Solution().maximumGap([1, 10])
print(res)

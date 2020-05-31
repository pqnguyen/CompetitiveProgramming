class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    def maxone(self, A, B):
        n = len(A)
        i, j = 0, 0  # start, end of current consecutive 1s sequence
        x, y = 0, 0  # start, end of longest consecutive 1s sequence
        while j < n:
            if A[j]:  # current element is 1
                if j - i > y - x:  # update start, end of longest 1s sequence
                    x, y = i, j
                j += 1  # move the right pointer
            elif not A[j] and B > 0:  # current element is 0, we can flip it
                if j - i > y - x:  # update start, end of longest 1s sequence
                    x, y = i, j
                B -= 1  # deacrese number of allowed flips
                j += 1  # move the right pointer
            else:  # current element is zero and we are out of flips
                if not A[i]:  # start of current 1s sequence is 0
                    B += 1  # increase available flips
                i += 1  # move the left pointer
        return list(range(x, y + 1))


A = [1, 1, 0, 1, 1, 1, 0]
res = Solution().maxone(A, 0)
print(res)

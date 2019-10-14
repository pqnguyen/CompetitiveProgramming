class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def subsets(self, A):
        A.sort()
        res = []
        self.subsetsHelper(A, 0, [], res)
        res.sort()
        return res

    def subsetsHelper(self, A, index, subset, res):
        if index == len(A):
            res.append(subset[:])
            return
        self.subsetsHelper(A, index + 1, subset, res)
        subset.append(A[index])
        self.subsetsHelper(A, index + 1, subset, res)
        subset.pop()


A = [15, 20, 12, 19, 4]
res = Solution().subsets(A)
print(res)

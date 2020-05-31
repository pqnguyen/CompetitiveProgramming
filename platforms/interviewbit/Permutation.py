class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def permute(self, A):
        res = []
        self.permuteHelper(A, 0, res)
        res.sort()
        return res

    def permuteHelper(self, A, index, res):
        if index == len(A):
            res.append(A[:])
            return
        for i in range(index, len(A)):
            A[index], A[i] = A[i], A[index]
            self.permuteHelper(A, index + 1, res)
            A[index], A[i] = A[i], A[index]


A = [1, 2, 3]
res = Solution().permute(A)
print(res)

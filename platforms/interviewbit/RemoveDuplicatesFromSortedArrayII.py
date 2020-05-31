class Solution:
    # @param A : list of integers
    # @return an integer
    def removeDuplicates(self, A):
        wall = 2
        for i in range(2, len(A)):
            if A[i] != A[wall - 2]:
                A[i], A[wall] = A[wall], A[i]
                wall += 1
        return wall


A = [1, 1, 1, 1, 2, 3, 4, 5, 5, 5, 6, 6]
res = Solution().removeDuplicates(A)
print(A[:res])

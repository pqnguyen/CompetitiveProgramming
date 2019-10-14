class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def removeElement(self, A, B):
        wall = 0
        for i in range(len(A)):
            if A[i] != B:
                A[i], A[wall] = A[wall], A[i]
                wall += 1
        return wall


A = [2, 4, 1, 1, 3, 1, 5]
res = Solution().removeElement(A, 1)
print(A[:res])

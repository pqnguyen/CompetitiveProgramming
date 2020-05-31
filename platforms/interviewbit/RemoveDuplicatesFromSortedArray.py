class Solution:
    # @param A : list of integers
    # @return an integer
    def removeDuplicates(self, A):
        if not A: return []
        wall = 1
        for i in range(1, len(A)):
            if A[i] != A[wall - 1]:
                A[wall], A[i] = A[i], A[wall]
                wall += 1
        return wall


A = [1, 2, 2, 3, 4, 4, 5]
res = Solution().removeDuplicates(A)
print(A[:res])

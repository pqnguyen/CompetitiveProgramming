class Solution:
    # @param A : list of integers
    # @param B : list of integers
    def merge(self, A, B):
        capacity = len(A) + len(B)
        i, j = len(A) - 1, len(B) - 1
        while len(A) < capacity: A.append(0)
        index = capacity - 1
        while j >= 0:
            if i >= 0 and A[i] > B[j]:
                A[index] = A[i]
                i -= 1
            else:
                A[index] = B[j]
                j -= 1
            index -= 1
        return A


A = [-4, 3]
B = [-2, -2]
Solution().merge(A, B)
print(A)
class Solution:
    # @param A : list of integers
    # @return A after the sort
    def sortColors(self, A):
        start, mid, end = 0, 0, len(A) - 1
        while mid <= end:
            if A[mid] == 0:
                A[start], A[mid] = A[mid], A[start]
                start += 1
                mid += 1
            elif A[mid] == 2:
                A[mid], A[end] = A[end], A[mid]
                end -= 1
            else:
                mid += 1
        return A


res = Solution().sortColors([0, 1, 2, 0, 1])
print(res)

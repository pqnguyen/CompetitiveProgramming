class Solution:
    # @param A : list of integers
    # @return a list of integers
    def subUnsort(self, A):
        sortedA = sorted(A)
        left, right = 0, len(A) - 1
        n = len(A)
        while left < n and A[left] == sortedA[left]: left += 1
        while right > -1 and A[right] == sortedA[right]: right -= 1
        return [left, right] if left < right else [-1]


res = Solution().subUnsort([5, 4, 3, 2])
print(res)

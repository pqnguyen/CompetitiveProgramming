# https://leetcode.com/problems/largest-perimeter-triangle/
class Solution:
    def largestPerimeter(self, A: List[int]) -> int:
        A.sort()
        for i in range(len(A) - 2, 0, -1):
            if A[i - 1] + A[i] > A[i + 1]:
                return A[i - 1] + A[i] + A[i + 1]
        return 0

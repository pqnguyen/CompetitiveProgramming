# https://leetcode.com/problems/monotonic-array/
from typing import List


class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        if not A or len(A) == 1: return True
        sign = 0
        for i in range(1, len(A)):
            if sign * (A[i] - A[i - 1]) < 0:
                return False
            if not sign:
                sign = A[i] - A[i - 1]
        return True

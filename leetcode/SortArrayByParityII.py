# https://leetcode.com/problems/sort-array-by-parity-ii/
from typing import List


class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        wall = i = 0
        while i < len(A):
            bothEven = wall % 2 == 0 and A[i] % 2 == 0
            bothOdd = wall % 2 == 1 and A[i] % 2 == 1
            if bothEven or bothOdd:
                A[wall], A[i] = A[i], A[wall]
                wall += 1
            else:
                i += 1
        return A


res = Solution().sortArrayByParityII([3, 1, 4, 2])
print(res)

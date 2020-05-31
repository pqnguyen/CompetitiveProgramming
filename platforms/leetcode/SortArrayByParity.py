# https://leetcode.com/problems/sort-array-by-parity/
from typing import List


class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        wall = 0
        for i in range(len(A)):
            if A[i] % 2 == 0:
                A[wall], A[i] = A[i], A[wall]
                wall += 1
        return A


res = Solution().sortArrayByParity([3, 1, 2, 4])
print(res)

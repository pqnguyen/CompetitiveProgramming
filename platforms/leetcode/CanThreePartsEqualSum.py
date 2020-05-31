# https://leetcode.com/problems/partition-array-into-three-parts-with-equal-sum/
from typing import List


class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        total = sum(A)
        if total % 3 != 0: return False
        sumPart = total // 3
        count = s = 0
        for i in range(len(A)):
            s += A[i]
            if s == sumPart:
                count += 1
                s = 0
        return count == 3

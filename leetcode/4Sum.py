import collections
from typing import List


class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        AB = collections.Counter(a + b for a in A for b in B)
        return sum(AB[-c-d] for c in C for d in D)


sol = Solution()
print(sol.fourSumCount([1, 2], [-2, -1], [-1, 2], [0, 2]))

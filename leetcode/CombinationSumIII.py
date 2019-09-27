import math
from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        self.combinationSum3Util(k, 0, 1, [0] * k, res, n)
        return res

    def combinationSum3Util(self, k, index, start, pattern, res, n):
        if n < 0: return
        if index == k:
            if n == 0: res.append(pattern[:])
            return

        for i in range(start, 10):
            pattern[index] = i
            self.combinationSum3Util(k, index + 1, i + 1, pattern, res, n - i)


res = Solution().combinationSum3(4, 20)
print(res)

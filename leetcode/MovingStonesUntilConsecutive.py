# https://leetcode.com/problems/moving-stones-until-consecutive/
from typing import List


class Solution:
    def numMovesStones(self, a: int, b: int, c: int) -> List[int]:
        a, b, c = sorted([a, b, c])
        tmp = 0
        if a == b - 1 and b + 1 == c:
            tmp = 0
        elif b - 1 - a <= 1 or c - b - 1 <= 1:
            tmp = 1
        else:
            tmp = 2
        res = [tmp]
        res.append(b - 1 - a + c - b - 1)
        return res


res = Solution().numMovesStones(4, 3, 2)
print(res)

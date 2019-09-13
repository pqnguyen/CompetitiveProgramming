# https://leetcode.com/problems/complement-of-base-10-integer/
import math


class Solution:
    def bitwiseComplement(self, N: int) -> int:
        if not N: return 1
        m = int(math.log(N, 2)) + 1
        return 2 ** m - 1 - N

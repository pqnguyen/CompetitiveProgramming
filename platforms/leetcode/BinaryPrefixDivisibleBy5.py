# https://leetcode.com/problems/binary-prefix-divisible-by-5/
class Solution:
    def prefixesDivBy5(self, A: List[int]) -> List[bool]:
        res = []
        n = 0
        for b in A:
            n = ((n << 1) | b) % 5
            res.append(n == 0)
        return res

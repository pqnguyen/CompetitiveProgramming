# https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/
from collections import defaultdict
from typing import List


class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        time = [duration % 60 for duration in time]
        f = defaultdict(int)
        res = 0
        for duration in time:
            if duration:
                res += f[60 - duration]
            else:
                res += f[0]
            f[duration] += 1
        return res


res = Solution().numPairsDivisibleBy60([60, 60, 60])
print(res)

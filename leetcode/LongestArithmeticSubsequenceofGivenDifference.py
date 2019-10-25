from bisect import bisect_left as lower_bound
from collections import defaultdict
from typing import List


class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dp = defaultdict(int)
        for i in range(len(arr)):
            dp[arr[i]] = dp[arr[i] - difference] + 1
        return max(dp.values())

from collections import defaultdict
from typing import List

MAX_INT = 2 ** 31 - 1


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if not n: return 0
        if n <= 2: return max(nums)
        dp = defaultdict(int)
        dp[0] = nums[0]
        for i in range(1, n):
            dp[i] = max(nums[i] + dp[i - 2], dp[i - 1])
        return max(dp.values())


print(Solution().rob([2, 1, 1, 2]))

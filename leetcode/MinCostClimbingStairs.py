from typing import List

MAX_INT = 2 ** 31 - 1


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        if n < 2: return 0
        dp = [MAX_INT] * n
        dp[0] = cost[0]
        dp[1] = cost[1]
        for i in range(2, n):
            dp[i] = cost[i] + min(dp[i - 1], dp[i - 2])
        return min(dp[n - 1], dp[n - 2])


res = Solution().minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1])
print(res)

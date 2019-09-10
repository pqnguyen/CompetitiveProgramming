# Cracking the coding interview - 8.1
# Triple Step: A child is running up a staircase with n steps and can hop
# either 1 step, 2 steps, or 3 steps at a time. Implement a method to count
# how many possible ways the child can run up the stairs.
from collections import defaultdict


class Solution:
    def triple_step(self, n):
        dp = defaultdict(int)
        dp[0] = 1
        return self.triple_step_util(n, dp)

    def triple_step_util(self, n, dp):
        if n < 0: return 0
        if dp[n]: return dp[n]
        dp[n] = self.triple_step_util(n - 1, dp) + self.triple_step_util(n - 2, dp) + self.triple_step_util(n - 3, dp)
        return dp[n]


print(Solution().triple_step(37))

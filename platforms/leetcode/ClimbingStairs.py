class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        ways = self.helper(n, memo)
        return ways

    def helper(self, n, memo):
        if n < 0: return 0
        if n == 0: return 1
        if n in memo: return memo[n]
        ways = self.helper(n - 1, memo) + self.helper(n - 2, memo)
        memo[n] = ways
        return memo[n]

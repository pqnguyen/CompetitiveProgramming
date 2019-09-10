# Cracking the coding interview - 8.11
# Coins: Given an infinite number of quarters (25 cents), dimes (10 cents), nickels (5 cents), and
# pennies (1 cent), write code to calculate the number of ways of representing n cents.
from collections import defaultdict

denoms = [25, 10, 5, 1]


class Solution:
    def make_change(self, n):
        if n == 0: return 0
        return self.make_change_util(n, 0)

    def make_change_util(self, n, start):
        if n == 0: return 1
        ways = 0
        for i in range(start, len(denoms)):
            cent = denoms[i]
            if n >= cent:
                ways += self.make_change_util(n - cent, i)
        return ways


class Solution1:
    def make_change(self, n):
        dp = defaultdict(dict)
        ways = self.make_change_util(n, 0, dp)
        return ways

    def make_change_util(self, n, index, dp):
        if index in dp[n]: return dp[n][index]
        if index >= len(denoms) - 1: return 1
        denom_amount = denoms[index]
        ways = i = 0
        while i * denom_amount <= n:
            remain = n - i * denom_amount
            ways += self.make_change_util(remain, index + 1, dp)
            i += 1
        dp[n][index] = ways
        return ways


res = Solution().make_change(100)
print(res)
res = Solution1().make_change(100)
print(res)

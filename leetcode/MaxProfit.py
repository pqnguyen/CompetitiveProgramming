# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_array = prices[:]
        for i in range(1, len(min_array)):
            min_array[i] = min(min_array[i], min_array[i - 1])

        profit = 0
        for i in range(1, len(prices)):
            profit = max(profit, prices[i] - min_array[i - 1])

        return profit

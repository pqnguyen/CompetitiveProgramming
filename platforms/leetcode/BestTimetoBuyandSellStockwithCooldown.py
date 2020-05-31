from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices: return 0
        n = len(prices)
        buy = [0] * n
        sell = [0] * n
        buy[0] = -prices[0]
        for i in range(1, len(prices)):
            price = prices[i]
            sell[i] = max(buy[i - 1] + price, sell[i - 1])
            buy[i] = max(sell[max(i - 2, 0)] - price, buy[i - 1])
        return max(sell)


prices = [1, 2, 3, 0, 2]
res = Solution().maxProfit(prices)
print(res)

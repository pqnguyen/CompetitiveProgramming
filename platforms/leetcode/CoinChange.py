from collections import deque
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort(reverse=False)
        visisted = {}
        queue = deque()
        queue.append((amount, 0))
        visisted[amount] = True

        while queue:
            amount, step = queue.popleft()
            if amount == 0: return step
            for coin in coins:
                if amount - coin >= 0 and amount - coin not in visisted:
                    queue.append((amount - coin, step + 1))
                    visisted[amount - coin] = True

        return -1


coins = [2]
amount = 11
print(Solution().coinChange(coins, amount))

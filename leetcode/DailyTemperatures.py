# https://leetcode.com/explore/learn/card/queue-stack/230/usage-stack/1363/
from collections import deque
from typing import List


class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        if not T: return []
        stack = deque()
        res = [0] * len(T)
        for index, temp in enumerate(T):
            while stack and stack[-1][0] < temp:
                top = stack.pop()
                res[top[1]] = index - top[1]
            stack.append((temp, index))
        return res


res = Solution().dailyTemperatures([])
print(res)

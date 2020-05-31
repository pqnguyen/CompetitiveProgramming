from collections import deque
from typing import List


class Solution:
    def trap(self, heights: List[int]) -> int:
        stack = deque()
        res = 0
        for i, height in enumerate(heights):
            while len(stack) > 1 and height > heights[stack[-1]]:
                bottom = stack.pop()
                res += (min(heights[stack[-1]], height) - heights[bottom]) * (i - stack[-1] - 1)

            if stack and height >= heights[stack[-1]]:
                stack.pop()

            if not stack or height < heights[stack[-1]]:
                stack.append(i)
        return res


res = Solution().trap([0, 5, 1, 1, 2, 3, 5])
print(res)

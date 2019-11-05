from collections import deque
from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        stack = deque()
        res = 0
        for i, height in enumerate(heights):
            while stack and height < heights[stack[-1]]:
                top = stack.pop()
                left = -1
                if stack: left = stack[-1]
                res = max(res, (i - left - 1) * heights[top])
            if not stack or height >= heights[stack[-1]]:
                stack.append(i)
        while stack:
            top = stack.pop()
            left = -1
            if stack: left = stack[-1]
            res = max(res, (n - left - 1) * heights[top])
        return res


heights = [2, 1, 5, 6, 2, 3]
res = Solution().largestRectangleArea(heights)
print(res)

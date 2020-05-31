from collections import deque
from typing import List


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix: return 0
        m, n = len(matrix), len(matrix[0])
        res = 0
        heights = [0] * n
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '0':
                    heights[j] = 0
                else:
                    heights[j] += 1
            res = max(res, self.largestRectangleArea(heights))
        return res

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


matrix = [
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]
res = Solution().maximalRectangle(matrix)
print(res)

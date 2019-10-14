from collections import deque


class Solution:
    # @param A : tuple of integers
    # @return an integer
    def trap(self, A):
        stack = deque()
        res = 0
        for i, bar in enumerate(A):
            if not stack or bar <= A[stack[-1]]:
                stack.append(i)
            else:
                while stack and bar >= A[stack[-1]]:
                    lastbar = stack.pop()
                    if len(stack): res += (min(bar, A[stack[-1]]) - A[lastbar]) * (i - stack[-1] - 1)
                stack.append(i)
        return res


A = [4, 2, 0, 3, 2, 5]
res = Solution().trap(A)
print(res)

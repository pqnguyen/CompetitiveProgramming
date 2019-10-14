from collections import deque


class Solution:
    # @param A : list of integers
    # @return an integer
    def largestRectangleArea(self, A):
        stack = deque()
        res = i = 0
        while i < len(A):
            if not stack or A[i] >= A[stack[-1]]:
                stack.append(i)
            else:
                while stack and A[i] < A[stack[-1]]:
                    top = stack.pop()
                    if stack:
                        res = max(res, A[top] * (i - stack[-1] - 1))
                    else:
                        res = max(res, A[top] * i)
                stack.append(i)
            i += 1
        while stack:
            top = stack.pop()
            if stack:
                res = max(res, A[top] * (i - stack[-1] - 1))
            else:
                res = max(res, A[top] * len(A))

        return res


A = [6, 2, 5, 4, 5, 1, 6]
res = Solution().largestRectangleArea(A)
print(res)

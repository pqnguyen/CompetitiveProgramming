from collections import deque


class Solution:
    # @param A : list of integers
    # @return a list of integers
    def prevSmaller(self, A):
        if not A: return []
        stack = deque()
        res = [-1] * len(A)
        stack.append(0)
        for i in range(1, len(A)):
            while stack and A[i] <= A[stack[-1]]: stack.pop()
            if stack and A[i] > A[stack[-1]]: res[i] = A[stack[-1]]
            stack.append(i)
        return res


exp = [39, 27, 11, 4, 24, 32, 32, 1]
res = Solution().prevSmaller(exp)
print(res)

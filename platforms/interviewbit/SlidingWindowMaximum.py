from collections import deque


class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return a list of integers
    def slidingMaximum(self, A, B):
        queue = deque()
        res = []
        for i in range(len(A)):
            if queue and i - queue[0][1] >= B: queue.popleft()
            self.push(queue, A[i], i)
            if i + 1 >= B: res.append(queue[0][0])
        return res

    def push(self, queue, val, index):
        while queue and queue[-1][0] <= val:
            queue.pop()
        queue.append((val, index))


A = [1, 3, -1, -3, 5, 3, 6, 7]
res = Solution().slidingMaximum(A, 3)
print(res)

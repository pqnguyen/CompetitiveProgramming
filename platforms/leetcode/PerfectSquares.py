# https://leetcode.com/explore/learn/card/queue-stack/231/practical-application-queue/1371/
from collections import deque, defaultdict


class Solution:
    def numSquares(self, n: int) -> int:
        squares = []
        i = 1
        while i * i <= n:
            squares.append(i * i)
            i += 1

        m = defaultdict(int)
        for square in squares: m[square] = 1
        queue = deque(squares)
        while queue:
            top = queue.popleft()
            if top == n: return m[top]
            for square in squares:
                if square + top <= n and not m[square + top]:
                    m[square + top] = m[top] + 1
                    queue.append(square + top)
        return -1

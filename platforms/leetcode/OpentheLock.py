# https://leetcode.com/explore/learn/card/queue-stack/231/practical-application-queue/1375/
from collections import defaultdict, deque
from typing import List


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        def neighbors(state):
            ls = list(map(int, state))
            for i in range(len(ls)):
                val = ls[i]
                ls[i] = ls[i] - 1 if ls[i] > 0 else 9
                yield "".join(map(str, ls))
                ls[i] = val
                ls[i] = ls[i] + 1 if ls[i] < 9 else 0
                yield "".join(map(str, ls))
                ls[i] = val

        root = "0000"
        visited = defaultdict(bool)
        for deadend in deadends: visited[deadend] = True
        if visited[target] or visited[root]: return -1
        queue = deque([(root, 0)])
        visited[root] = True
        while queue:
            top, times = queue.popleft()
            if top == target: return times
            for neighbor in neighbors(top):
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append((neighbor, times + 1))

        return -1


res = Solution().openLock(["0000"], "8888")
print(res)

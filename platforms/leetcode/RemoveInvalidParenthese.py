from collections import deque
from typing import List


class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        queue = deque()
        visited = set()
        queue.append(s)
        visited.add(s)
        res = []
        level = False
        while queue:
            s = queue.popleft()
            if self.isValid(s):
                res.append(s)
                level = True
            if level: continue

            for i in range(len(s)):
                if s[i] not in {'(', ')'}: continue
                ns = s[:i] + s[i + 1:]
                if ns not in visited:
                    queue.append(ns)
                    visited.add(ns)
        return res

    def isValid(self, s):
        count = 0
        for ch in s:
            if ch == '(':
                count += 1
            elif ch == ')':
                count -= 1
            if count < 0: return False
        return count == 0


res = Solution().removeInvalidParentheses("())")
print(res)

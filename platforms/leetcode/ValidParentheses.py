# https://leetcode.com/problems/valid-parentheses/
from collections import deque


class Solution:
    def isValid(self, s: str) -> bool:
        m = {')': '(', '}': '{', ']': '['}
        stack = deque()
        for ch in s:
            if ch in m:
                if not stack or stack[-1] != m[ch]:
                    return False
                stack.pop()
            else:
                stack.append(ch)
        return not stack

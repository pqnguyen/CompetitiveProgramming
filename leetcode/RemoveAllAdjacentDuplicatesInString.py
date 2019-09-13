# https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/
from collections import deque


class Solution:
    def removeDuplicates(self, S: str) -> str:
        stack = deque()
        for ch in S:
            if len(stack) and ch == stack[-1]:
                stack.pop()
            else:
                stack.append(ch)
        return "".join(stack)

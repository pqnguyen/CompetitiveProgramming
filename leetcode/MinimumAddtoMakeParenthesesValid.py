from collections import deque


class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        stack = deque()
        for p in S:
            isAdd = True
            if p == ')':
                if stack and stack[-1] == '(':
                    stack.pop()
                    isAdd = False

            if isAdd:
                stack.append(p)
        return len(stack)


res = Solution().minAddToMakeValid("()))((")
print(res)

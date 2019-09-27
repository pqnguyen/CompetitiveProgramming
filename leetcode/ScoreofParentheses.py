from collections import deque


class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        stack = deque()
        for s in S:
            if s == ')':
                total = 0
                while stack:
                    top = stack.pop()
                    if top == '(': break
                    total += int(top)
                stack.append(str(2 * total) if total else '1')
            else:
                stack.append(s)
        total = sum(map(int, stack))
        return total


s = '(()(()))'
res = Solution().scoreOfParentheses(s)
print(res)

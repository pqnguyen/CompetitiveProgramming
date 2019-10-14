from collections import deque


class Solution:
    # @param A : string
    # @return an integer
    def braces(self, A):
        stack = deque()
        for ch in A:
            if ch != ')':
                stack.append(ch)
            else:
                valid = False
                while stack and stack[-1] != '(':
                    temp = stack.pop()
                    if temp in {'+', '-', '*', '/'}:
                        valid = True
                if stack: stack.pop()
                if not valid: return 0
        return 1


exp = "((a + (a + b)) + c)"
res = Solution().braces(exp)
print(res)

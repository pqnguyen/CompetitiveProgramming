from collections import deque


class Solution:
    # @param A : string
    # @return an integer
    def isValid(self, A):
        parentheses = {')': '(', ']': '[', '}': '{'}
        stack = deque()
        for ch in A:
            if ch in parentheses:
                if not stack or stack[-1] != parentheses[ch]: return 0
                stack.pop()
            else:
                stack.append(ch)
        return 1 if len(stack) == 0 else 0


res = Solution().isValid("()[]{}{]")
print(res)

# https://leetcode.com/explore/learn/card/queue-stack/230/usage-stack/1394/
from collections import deque
from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = deque()
        for token in tokens:
            if token in ('+', '-', '*', '/'):
                second, first = int(stack.pop()), int(stack.pop())
                tmp = 0
                if token == '+':
                    tmp = first + second
                elif token == '-':
                    tmp = first - second
                elif token == '*':
                    tmp = first * second
                else:
                    tmp = int(first / second)
                stack.append(str(tmp))
            else:
                stack.append(token)
        if stack:
            return int(stack.pop())
        return -1


res = Solution().evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"])
print(res)

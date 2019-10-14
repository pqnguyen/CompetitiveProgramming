from collections import deque


class MinStack:
    # @param x, an integer
    def __init__(self):
        self.stack = deque()

    def push(self, x):
        mi = x
        if self.stack: mi = min(self.stack[-1][1])
        self.stack.append((x, mi))

    # @return nothing
    def pop(self):
        if self.stack: self.stack.pop()

    # @return an integer
    def top(self):
        if not self.stack: return -1
        return self.stack[-1][0]

    # @return an integer
    def getMin(self):
        if not self.stack: return -1
        return self.stack[-1][1]


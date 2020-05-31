# https://leetcode.com/explore/learn/card/queue-stack/230/usage-stack/1360/
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x: int) -> None:
        m = x
        if self.stack: m = min(m, self.stack[-1][1])
        self.stack.append((x, m))

    def pop(self) -> None:
        if self.stack: self.stack.pop()

    def top(self) -> int:
        if self.stack: return self.stack[-1][0]
        return -1

    def getMin(self) -> int:
        if self.stack: return self.stack[-1][1]
        return -1

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
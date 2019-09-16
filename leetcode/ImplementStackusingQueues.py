# https://leetcode.com/explore/learn/card/queue-stack/239/conclusion/1387/
from collections import deque


class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue1 = deque()
        self.queue2 = deque()

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        if self.queue1: self.queue2.append(self.queue1.popleft())
        self.queue2.append(x)

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        if self.empty(): return -1
        self.transfer()
        return self.queue1.pop()

    def top(self) -> int:
        """
        Get the top element.
        """
        if self.empty(): return -1
        self.transfer()
        return self.queue1[0]

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return not self.queue1 and not self.queue2

    def transfer(self):
        if not self.queue1:
            self.queue1, self.queue2 = self.queue2, self.queue1
        while len(self.queue1) > 1:
            self.queue2.append(self.queue1.popleft())

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()

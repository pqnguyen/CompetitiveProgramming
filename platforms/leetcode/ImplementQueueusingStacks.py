from collections import deque as stack


class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.inbound = stack()
        self.outbound = stack()

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.inbound.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if self.empty(): return -1
        self.inboundToOutbound()
        return self.outbound.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        if self.empty(): return -1
        self.inboundToOutbound()
        return self.outbound[-1]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return not self.inbound and not self.outbound

    def inboundToOutbound(self):
        if not self.outbound:
            while self.inbound:
                self.outbound.append(self.inbound.pop())

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

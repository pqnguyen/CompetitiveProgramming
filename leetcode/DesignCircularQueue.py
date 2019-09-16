# https://leetcode.com/explore/learn/card/queue-stack/228/first-in-first-out-data-structure/1337/
class MyCircularQueue:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self.queue = [0] * k
        self.MAX_SIZE = k
        self.head = self.tail = -1

    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        if self.isFull(): return False
        if self.head == self.tail == -1:
            self.head = self.tail = 0
        elif self.tail == self.MAX_SIZE - 1:
            self.tail = 0
        else:
            self.tail += 1
        self.queue[self.tail] = value
        return True

    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        if self.isEmpty(): return False
        if self.head == self.tail:
            self.head = self.tail = -1
        elif self.head == self.MAX_SIZE - 1:
            self.head = 0
        else:
            self.head += 1
        return True

    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        if self.isEmpty(): return -1
        return self.queue[self.head]

    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        if self.isEmpty(): return -1
        return self.queue[self.tail]

    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        if self.head == self.tail == -1: return True
        return False

    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        if self.head == self.tail == -1: return False
        size = 0
        if self.head < self.tail:
            size = self.tail - self.head + 1
        else:
            size = self.MAX_SIZE - self.head + self.tail + 1
        return size == self.MAX_SIZE

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()

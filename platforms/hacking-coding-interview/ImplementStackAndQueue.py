# Implement Stack


class StackNode:
    def __init__(self, val):
        self.value = val
        self.next = None


class Stack:
    def __init__(self):
        self.head = None
        self.size = 0

    def pop(self):
        tmp = self.head
        if self.head:
            self.head = self.head.next
            self.size -= 1
        return tmp

    def push(self, val):
        node = StackNode(val)
        node.next = self.head
        self.head = node
        self.size += 1

    def peek(self):
        if self.head:
            return self.head.value
        return None

    def is_empty(self):
        return self.size == 0

    def size(self):
        return self.size


class QueueNode:
    def __init__(self, val):
        self.value = val
        self.next = None


class Queue:
    def __init__(self):
        self.head = self.tail = None
        self.size = 0

    def add(self, val):
        node = QueueNode(val)
        if not self.head:
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.size += 1

    def remove(self):
        tmp = self.head
        if self.head:
            self.head = self.head.next
            self.size -= 1
        return tmp

    def peek(self):
        return self.head.value if self.head else None

    def is_empty(self):
        return self.size == 0

    def size(self):
        return self.size


print("test stack")
stack = Stack()
stack.push(1)
stack.push(2)
print(stack.peek() == 2)
stack.pop()
print(stack.peek() == 1)
stack.pop()
print(stack.peek() is None)

print("test queue")
queue = Queue()
queue.add(1)
queue.add(2)
print(queue.peek() == 1)
queue.remove()
print(queue.peek() == 2)
queue.remove()
print(queue.peek() is None)

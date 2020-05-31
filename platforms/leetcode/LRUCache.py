class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None


class LinkedList:
    def __init__(self):
        self.head = Node(None, None)
        self.tail = Node(None, None)
        self.head.next = self.tail
        self.tail.prev = self.head

    def insert(self, node):
        next = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = next
        next.prev = node

    def delete(self, node):
        if not node: return None
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev
        node.prev = node.next = None
        return node

    def pop(self):
        if self.isEmpty(): return None
        node = self.tail.prev
        self.delete(node)
        return node

    def move2top(self, node):
        self.delete(node)
        self.insert(node)

    def isEmpty(self):
        return self.head.next == self.tail


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.tb = {}
        self.ll = LinkedList()

    def get(self, key: int) -> int:
        if key not in self.tb: return -1
        node = self.tb[key]
        self.ll.move2top(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        self.delete(key)
        if self.isFull(): self.evict()
        node = Node(key, value)
        self.ll.insert(node)
        self.tb[key] = node

    def delete(self, key):
        if key in self.tb:
            node = self.tb[key]
            self.ll.delete(node)
            del self.tb[key]

    def isFull(self):
        return len(self.tb) == self.capacity

    def evict(self):
        last_node = self.ll.pop()
        if not last_node: return
        del self.tb[last_node.key]


cache = LRUCache(2)
cache.put(1, 1)
cache.put(2, 2)
print(cache.get(1))  # returns 1
cache.put(3, 3)  # evicts key 2
print(cache.get(2))  # returns -1 (not found)
cache.put(4, 4)  # evicts key 1
print(cache.get(1))  # returns -1 (not found)
print(cache.get(3))  # returns 3
print(cache.get(4))  # returns 4

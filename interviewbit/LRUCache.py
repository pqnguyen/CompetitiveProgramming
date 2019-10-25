class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = self.prev = None


class LinkList:
    def __init__(self):
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.sz = 0

    def move2head(self, node):
        self.remove(node)
        self._insert(node)

    def remove(self, node):
        self.sz -= 1
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev
        node.next = None
        node.prev = None
        return node

    def size(self):
        return self.sz

    def removeLast(self):
        prev = self.tail.prev
        return self.remove(prev)

    def insert(self, key, value):
        node = Node(key, value)
        self._insert(node)
        return node

    def _insert(self, node):
        self.sz += 1
        next = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = next
        next.prev = node
        return node


class LRUCache:

    # @param capacity, an integer
    def __init__(self, capacity):
        self.capacity = capacity
        self.tb = {}
        self.ls = LinkList()

    # @return an integer
    def get(self, key):
        if key not in self.tb: return -1
        node = self.tb[key]
        self.ls.move2head(node)
        return node.val

    def set(self, key, value):
        if key in self.tb:
            node = self.tb[key]
            self.ls.remove(node)
            del self.tb[key]
        if self.ls.size() == self.capacity:
            node = self.ls.removeLast()
            del self.tb[node.key]
        node = self.ls.insert(key, value)
        self.tb[key] = node


cache = LRUCache(3)
print(cache.get(1))
cache.set(1, 1)
cache.set(2, 2)
cache.set(3, 3)
print(cache.get(1))
cache.set(4, 4)
print(cache.get(2))

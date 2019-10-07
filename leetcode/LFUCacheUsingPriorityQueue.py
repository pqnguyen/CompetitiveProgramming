time = 0


def getTime():
    global time
    time += 1
    return time


class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.freq = 0
        self.time = getTime()

    def __str__(self):
        return f"{self.key}:{self.val}:{self.freq}"


class PriorityQueue:
    def __init__(self):
        self.a = []
        self.tb = {}
        self.size = 0

    def up(self, i):
        if i == 0: return
        while (i - 1) // 2 >= 0:
            if self.less(self.a[i], self.a[(i - 1) // 2]):
                self.swap(i, (i - 1) // 2)
                i = (i - 1) // 2
            else:
                break

    def down(self, i):
        while 2 * i + 1 < self.size:
            min_idx = i
            if 2 * i + 1 < self.size and self.less(self.a[2 * i + 1], self.a[min_idx]):
                min_idx = 2 * i + 1

            if 2 * i + 2 < self.size and self.less(self.a[2 * i + 2], self.a[min_idx]):
                min_idx = 2 * i + 2

            if i != min_idx:
                self.swap(i, min_idx)
                i = min_idx
            else:
                break

    def insert(self, node):
        self.a.append(node)
        self.size += 1
        self.tb[node.key] = self.size - 1
        self.up(self.size - 1)

    def pop(self):
        if self.isEmpty(): return None
        self.swap(0, self.size - 1)
        self.size -= 1
        node = self.a.pop()
        del self.tb[node.key]
        self.down(0)
        return node

    def increase(self, node):
        node.freq += 1
        node.time = getTime()
        i = self.tb[node.key]
        self.down(i)

    def reset(self, key, val):
        node = self.getNode(key)
        if not node: return
        node.val = val
        node.time = getTime()
        node.freq += 1
        i = self.tb[key]
        self.down(i)

    def isEmpty(self):
        return self.size == 0

    def less(self, node1, node2):
        if node1.freq == node2.freq:
            return node1.time < node2.time
        return node1.freq < node2.freq

    def swap(self, idx1, idx2):
        node1, node2 = self.a[idx1], self.a[idx2]
        self.tb[node1.key] = idx2
        self.tb[node2.key] = idx1
        self.a[idx1], self.a[idx2] = node2, node1

    def exist(self, key):
        return key in self.tb

    def getNode(self, key):
        if not self.exist(key): return None
        i = self.tb[key]
        return self.a[i]

    def getSize(self):
        return self.size


class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.pq = PriorityQueue()

    def get(self, key: int) -> int:
        node = self.pq.getNode(key)
        if not node: return -1
        self.pq.increase(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0: return
        if self.pq.exist(key):
            self.pq.reset(key, value)
            return
        size = self.pq.getSize()
        if size == self.capacity:
            self.pq.pop()
        self.pq.insert(Node(key, value))


cmds = ["LFUCache", "put", "put", "put", "put", "put", "get", "put", "get", "get", "put", "get", "put", "put", "put",
        "get", "put", "get", "get", "get", "get", "put", "put", "get", "get", "get", "put", "put", "get", "put", "get",
        "put", "get", "get", "get", "put", "put", "put", "get", "put", "get", "get", "put", "put", "get", "put", "put",
        "put", "put", "get", "put", "put", "get", "put", "put", "get", "put", "put", "put", "put", "put", "get", "put",
        "put", "get", "put", "get", "get", "get", "put", "get", "get", "put", "put", "put", "put", "get", "put", "put",
        "put", "put", "get", "get", "get", "put", "put", "put", "get", "put", "put", "put", "get", "put", "put", "put",
        "get", "get", "get", "put", "put", "put", "put", "get", "put", "put", "put", "put", "put", "put", "put"]
data = [[10], [10, 13], [3, 17], [6, 11], [10, 5], [9, 10], [13], [2, 19], [2], [3], [5, 25], [8], [9, 22], [5, 5],
        [1, 30], [11], [9, 12], [7], [5], [8], [9], [4, 30], [9, 3], [9], [10], [10], [6, 14], [3, 1], [3], [10, 11],
        [8], [2, 14], [1], [5], [4], [11, 4], [12, 24], [5, 18], [13], [7, 23], [8], [12], [3, 27], [2, 12], [5],
        [2, 9], [13, 4], [8, 18], [1, 7], [6], [9, 29], [8, 21], [5], [6, 30], [1, 12], [10], [4, 15], [7, 22],
        [11, 26], [8, 17], [9, 29], [5], [3, 4], [11, 30], [12], [4, 29], [3], [9], [6], [3, 4], [1], [10], [3, 29],
        [10, 28], [1, 20], [11, 13], [3], [3, 12], [3, 8], [10, 9], [3, 26], [8], [7], [5], [13, 17], [2, 27], [11, 15],
        [12], [9, 19], [2, 15], [3, 16], [1], [12, 17], [9, 1], [6, 19], [4], [5], [5], [8, 1], [11, 7], [5, 2],
        [9, 28], [1], [2, 2], [7, 4], [4, 22], [7, 24], [9, 26], [13, 28], [11, 26]]

cache = None
for i, cmd in enumerate(cmds):
    if cmd == "LFUCache":
        cache = LFUCache(data[i][0])
    elif cmd == "put":
        cache.put(data[i][0], data[i][1])
        print("null,", end="")
    else:
        print(cache.get(data[i][0]), end=',')

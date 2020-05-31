class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = self.tail = None

    def append(self, val):
        node = Node(val)
        if self.head is None:
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def delete(self, val):
        if not self.head: return False
        prev = None
        cur = self.head
        while cur:
            if cur.val == val:
                if cur == self.tail: self.tail = prev

                if prev:
                    prev.next = cur.next
                else:
                    self.head = cur.next
                    if not self.head: self.tail = None
                return True
            prev = cur
            cur = cur.next
        return False

    def insert_after(self, val, inserted_val):
        ptr = self.search(val)
        if ptr:
            node = Node(inserted_val)
            if ptr == self.tail: self.tail = node
            node.next = ptr.next
            ptr.next = node
            return True
        return False

    def search(self, val):
        ptr = self.head
        while ptr:
            if ptr.val == val: return ptr
            ptr = ptr.next
        return None

    def traversal(self):
        ptr = self.head
        while ptr:
            print(ptr.val, end=' ')
            ptr = ptr.next
        print()


ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.traversal()  # 1 2 3 4

ll.insert_after(4, 5)
ll.traversal()  # 1 2 3 4 5

ll.insert_after(2, 6)
ll.traversal()  # 1 2 6 3 4 5

ll.delete(1)
ll.traversal()  # 2 6 3 4 5

ll.delete(6)
ll.traversal()  # 2 3 4 5

ll.delete(5)
ll.traversal()  # 2 3 4

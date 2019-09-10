# Cracking the coding interview - 2.1


class Node:
    def __init__(self, val):
        self.value = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, val):
        node = Node(val)
        if not self.head:
            self.head = node
        else:
            ptr = self.head
            while ptr.next:
                ptr = ptr.next

            ptr.next = node

    def traversal(self):
        ptr = self.head
        while ptr:
            print(ptr.value, end=' ')
            ptr = ptr.next
        print()


# Using set for checking a value that was already appended to a new linked list
class Solution1:
    def init(self):
        ll = LinkedList()
        for val in [4, 4, 3, 2, 2, 1, 1]:
            ll.append(val)

        result = self.solve(ll)
        result.traversal()  # 4 3 2 1

    def solve(self, ll):
        unique = set()
        result = LinkedList()
        ptr = ll.head
        while ptr:
            if ptr.value not in unique:
                unique.add(ptr.value)
                result.append(ptr.value)
            ptr = ptr.next

        return result


# using two pointers that one is traversal, the another run before the first pointer for checking duplicated
class Solution2:
    def init(self):
        ll = LinkedList()
        for val in [4, 4, 4, 2, 3, 1, 1, 1]:
            ll.append(val)

        result = self.solve(ll)
        result.traversal()  # 4 2 3 1

    def solve(self, ll):
        root = ll.head
        while root:
            prev = root
            cur = root.next
            while cur:
                if cur.value == root.value:
                    prev.next = cur.next
                    cur = cur.next
                else:
                    prev = cur
                    cur = cur.next

            root = root.next
        return ll


# The input must be sorted
# Using two pointer, one before another, if the value is the same, we remove the node
class Solution3:
    def init(self):
        ll = LinkedList()
        for val in [1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 4]:
            ll.append(val)

        result = self.solve(ll)
        result.traversal()  # 1 2 3 4

    def solve(self, ll):
        root = ll.head
        cur = root.next
        while cur:
            if cur.value == root.value:
                root.next = cur.next
            else:
                root = cur
            cur = cur.next

        return ll


# Solution1().init()
# Solution2().init()
Solution3().init()

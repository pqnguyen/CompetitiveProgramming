# Cracking the coding interview - 2.4
# Write code to partition a linked list around a value x,
# such that all nodes less than x come before all nodes greater than or equal to x


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


class Solution:
    def init(self):
        ll = LinkedList()
        for val in [3, 5, 8, 5, 10, 2, 1]:
            ll.append(val)
        res = self.solve(ll, 2)
        res.traversal()

    def solve(self, ll, pivot):
        wall = ptr = ll.head
        while ptr:
            if ptr.value < pivot:
                wall.value, ptr.value = ptr.value, wall.value
                wall = wall.next
            ptr = ptr.next
        return ll


Solution().init()

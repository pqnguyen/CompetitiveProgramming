# Cracking the coding interview - 2.5

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
        a = LinkedList()
        for val in [7, 1, 6]:
            a.append(val)

        b = LinkedList()
        for val in [9, 5]:
            b.append(val)

        res = self.solve(a, b)
        res.traversal()

    def solve(self, a, b):
        result = LinkedList()
        carry_over = 0
        ptra = a.head
        ptrb = b.head
        while ptra and ptrb:
            s = ptra.value + ptrb.value + carry_over
            result.append(s % 10)
            carry_over = s // 10
            ptra = ptra.next
            ptrb = ptrb.next

        while ptra:
            s = ptra.value + carry_over
            result.append(s % 10)
            carry_over = s // 10
            ptra = ptra.next

        while ptrb:
            s = ptrb.value + carry_over
            result.append(s % 10)
            carry_over = s // 10
            ptrb = ptrb.next

        if carry_over:
            result.append(carry_over)

        return result


Solution().init()

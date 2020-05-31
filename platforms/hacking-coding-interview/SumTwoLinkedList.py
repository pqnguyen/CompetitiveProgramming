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

    def append_head(self, val):
        node = Node(val)
        if not self.head:
            self.head = node
        else:
            node.next = self.head
            self.head = node

    def traversal(self):
        ptr = self.head
        while ptr:
            print(ptr.value, end=' ')
            ptr = ptr.next
        print()

    def length(self):
        length = 0
        ptr = self.head
        while ptr:
            length += 1
            ptr = ptr.next
        return length


class Solution:
    def init(self):
        a = LinkedList()
        for val in [6, 1, 7]:
            a.append(val)

        b = LinkedList()
        for val in [2, 9]:
            b.append(val)

        res = self.solve(a, b)
        res.traversal()

    def solve(self, a, b):
        length_a = a.length()
        length_b = b.length()
        if length_a > length_b:
            self.pad_zero(b, length_a - length_b)
        else:
            self.pad_zero(a, length_b - length_a)

        res, carry_over = self.sum_util(a.head, b.head)
        if carry_over:
            res.append_head(carry_over)
        return res

    def sum_util(self, a, b):
        if not a and not b:
            return LinkedList(), 0
        head, carry_over = self.sum_util(a.next, b.next)
        s = a.value + b.value + carry_over
        head.append_head(s % 10)
        return head, s // 10

    def pad_zero(self, a, num):
        for i in range(num):
            a.append_head(0)


Solution().init()

# Cracking the coding interview - 2.3
# Implement an algorithm-cpp to delete middle node of a single linked list, given only access to that node
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
        for val in [1]:
            ll.append(val)
        res = self.solve(ll)
        res.traversal()

    def solve(self, ll):
        node = self.find_middle_node(ll)
        next_node = node.next
        if next_node:
            node.value = next_node.value
            node.next = next_node.next
        return ll

    def find_middle_node(self, ll):
        p1 = p2 = ll.head
        while p2:
            p2 = p2.next
            if p2:
                p2 = p2.next
            else:
                break

            if p2:
                p1 = p1.next

        return p1


Solution().init()

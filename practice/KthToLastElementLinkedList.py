# Cracking the coding interview - 2.2
# Implement an algorithm to find the kth-to-last element of a single linked list


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
    def init(self, kth):
        ll = LinkedList()
        for val in [9, 8, 7, 6, 5, 4, 3, 2, 1]:
            ll.append(val)
        res = self.solve(ll, kth)
        print(res)

    def solve(self, ll, kth):
        if kth < 1: return None
        p1 = p2 = ll.head
        distance = 0
        while p1:
            p1 = p1.next
            if distance < kth:
                distance += 1
            else:
                p2 = p2.next

        if distance == kth:
            return p2.value
        else:
            return None


Solution().init(2)
Solution().init(10)

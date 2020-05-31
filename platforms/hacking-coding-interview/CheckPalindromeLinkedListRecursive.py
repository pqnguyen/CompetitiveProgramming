# Cracking the coding interview - 2.6

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
        ll = LinkedList()
        for val in [1, 1, 2, 1, 1]:
            ll.append(val)

        self.solve(ll)

    def solve(self, ll):
        self.left = ll.head
        is_palindrome = self.check_palindrome(ll.head)
        print(is_palindrome)
        return is_palindrome

    def check_palindrome(self, right):
        if not right:
            return True
        is_palindrome = self.check_palindrome(right.next) and self.left.value == right.value
        if not is_palindrome:
            return False
        self.left = self.left.next
        return True


Solution().init()

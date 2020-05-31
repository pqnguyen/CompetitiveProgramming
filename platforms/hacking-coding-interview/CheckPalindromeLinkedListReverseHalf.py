# Cracking the coding interview - 2.6
# https://www.techiedelight.com/check-if-linked-list-is-palindrome/

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
    def solve(self):
        ll = LinkedList()
        for val in [1]:
            ll.append(val)

        print(self.is_palindrome(ll))

    def is_palindrome(self, ll):
        if not ll.head or not ll.head.next: return True
        middle_node = self.find_middle(ll)
        reversed_ll = self.reverse(middle_node)
        return self.compare(ll.head, reversed_ll)

    def find_middle(self, ll):
        prev = None
        slow = fast = ll.head
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        prev.next = None
        if fast:
            slow = slow.next

        return slow

    def reverse(self, node):
        prev, cur = None, node
        while cur:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        return prev

    def compare(self, ll, reversed_ll):
        if not ll and not reversed_ll: return True
        return ll.value == reversed_ll.value and self.compare(ll.next, reversed_ll.next)


Solution().solve()

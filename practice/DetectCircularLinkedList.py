# Cracking the coding interview - 2.8

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

    def search(self, val):
        ptr = self.head
        while ptr:
            if ptr.value == val:
                return ptr
            ptr = ptr.next
        return None

    def get_last_node(self):
        ptr = self.head
        while ptr and ptr.next:
            ptr = ptr.next
        return ptr


class Solution:
    def solve(self):
        ll = LinkedList()
        for val in [1, 2, 3, 4, 5]:
            ll.append(val)

        beginning_node = ll.search(5)
        last_node = ll.get_last_node()
        last_node.next = beginning_node

        res = self.node_beginning_loop(ll)
        print(res.value)

    def node_beginning_loop(self, ll):
        # no loop when empty linked list or single node
        if not ll.head or not ll.head.next:
            return None

        slow = fast = ll.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast: break

        # there is no loop
        if slow != fast: return None

        slow = ll.head
        while slow != fast:
            slow = slow.next
            fast = fast.next

        return slow


Solution().solve()

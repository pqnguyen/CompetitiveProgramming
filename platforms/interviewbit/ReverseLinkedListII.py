# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def array2list(a):
    if not a: return None
    current = head = ListNode(a[0])
    for i in range(1, len(a)):
        current.next = ListNode(a[i])
        current = current.next
    return head


def traversal(a):
    while a:
        print(a.val, end=" ")
        a = a.next


# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @param C : integer
    # @return the head node in the linked list
    def reverseBetween(self, A, B, C):
        first, last = None, A
        while B > 1:
            first = first.next if first else A
            if not first: return A
            B -= 1
        while C > 1 and last and last.next:
            C -= 1
            last = last.next
        nextLast = last.next
        nextFirst = first.next if first else A
        head = self.reverse(nextFirst, last)
        nextFirst.next = nextLast
        if first:
            first.next = head
        else:
            A = head
        return A

    def reverse(self, start, end):
        if start == end or not start.next: return start
        prev, next = start, start.next
        while True:
            nextnext = next.next
            next.next = prev
            prev = next
            next = nextnext
            if prev == end: break
        start.next = None
        return prev


a = [1, 2, 3, 4, 5, 6, 7]
head = array2list(a)
head = Solution().reverseBetween(head, 7, 7)
traversal(head)

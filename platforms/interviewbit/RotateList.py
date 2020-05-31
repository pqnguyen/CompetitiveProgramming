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
    # @return the head node in the linked list
    def rotateRight(self, A, B):
        if not A: return None
        B = B % self.length(A)
        if not B: return A
        slow, fast = A, A
        while B and fast and fast.next:
            B -= 1
            fast = fast.next
        if B: return A
        while fast and fast.next:
            fast = fast.next
            slow = slow.next
        nextHead = slow.next
        slow.next = None
        fast.next = A
        return nextHead

    def length(self, A):
        length = 0
        while A:
            length += 1
            A = A.next
        return length


a = [91, 34, 18, 83, 38, 82, 21, 69]
head = array2list(a)
head = Solution().rotateRight(head, 8)
traversal(head)

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
    # @param B : head node of linked list
    # @return the head node in the linked list
    def addTwoNumbers(self, A, B):
        self.head = self.tail = self.faketail = None
        carry = 0
        while A or B:
            a, b = 0, 0
            if A: a = A.val
            if B: b = B.val
            total = a + b + carry
            self.insert(total % 10)
            carry = total // 10
            if A: A = A.next
            if B: B = B.next
        if carry:
            self.insert(carry)
        self.tail.next = None
        return self.head

    def insert(self, val):
        node = ListNode(val)
        if self.faketail is None:
            self.head = self.faketail = node
        else:
            self.faketail.next = node
            self.faketail = node
        if node.val:
            self.tail = node


A = array2list([2, 4, 3, 0, 0, 0, 0])
B = array2list([5, 6, 4])
head = Solution().addTwoNumbers(A, B)
traversal(head)

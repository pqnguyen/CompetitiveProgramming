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


# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : head node of linked list
    # @return the head node in the linked list
    def mergeTwoLists(self, A, B):
        head = tail = ListNode(-1)
        while A and B:
            node = None
            if A.val > B.val:
                node = B
                B = B.next
            else:
                node = A
                A = A.next
            node.next = None
            if tail is None:
                head = tail = node
            else:
                tail.next = node
                tail = node
        if A:
            tail.next = A
        else:
            tail.next = B

        return head.next

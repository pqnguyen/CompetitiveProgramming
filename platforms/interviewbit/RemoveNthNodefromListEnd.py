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
    def removeNthFromEnd(self, A, B):
        slow, fast = None, A
        while B and fast:
            B -= 1
            fast = fast.next
        while fast:
            slow = slow.next if slow else A
            fast = fast.next
        if slow:
            nextslow = slow.next
            slow.next = nextslow.next
            nextslow.next = None
        else:
            A = A.next
        return A


a = [1, 2, 3, 4, 5, 6]
head = array2list(a)
head = Solution().removeNthFromEnd(head, 2)
traversal(head)

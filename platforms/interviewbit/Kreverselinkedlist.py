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


class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
    def reverseList(self, A, B):
        head = tail = None
        while A:
            h1, t1, next = self.reverseKelemens(A, B)
            if tail is None:
                head, tail = h1, t1
            else:
                tail.next = h1
                tail = t1
            A = next
        return head

    def reverseKelemens(self, A, K):
        prev, next = None, A
        nextnext = next.next
        while K:
            nextnext = next.next
            next.next = prev
            prev = next
            next = nextnext
            K -= 1
        return prev, A, nextnext


head = array2list([1, 2, 3, 4, 5, 6])
head = Solution().reverseList(head, 3)
# traversal(head)

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
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def swapPairs(self, A):
        current = A
        while current and current.next:
            current.val, current.next.val = current.next.val, current.val
            current = current.next.next
        return A


head = array2list([1, 2, 3, 4, 5])
head = Solution().swapPairs(head)
traversal(head)

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
    # @return the head node in the linked list
    def insertionSortList(self, A):
        head = ListNode(-2 ** 31)
        current = A
        while current:
            node = ListNode(current.val)
            insertedPos = head
            while insertedPos.next and insertedPos.next.val < node.val:
                insertedPos = insertedPos.next

            next = insertedPos.next
            insertedPos.next = node
            node.next = next
            current = current.next
        return head.next


a = [1, 4, 3, 2, 5, 2, 3]
head = array2list(a)
head = Solution().insertionSortList(head)
traversal(head)

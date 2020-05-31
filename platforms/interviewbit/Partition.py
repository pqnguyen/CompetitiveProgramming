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
    def partition(self, A, B):
        fakeHead = ListNode(0)
        fakeHead.next = A
        wall = current = fakeHead
        while current and current.next:
            if current.next.val < B:
                if current != wall:
                    node = current.next
                    current.next = node.next
                    node.next = None

                    nextWall = wall.next
                    wall.next = node
                    node.next = nextWall
                    wall = node
                else:
                    wall = wall.next
                    current = current.next
            else:
                current = current.next
        return fakeHead.next


a = [1, 4, 3, 2, 5, 2, 3]
head = array2list(a)
head = Solution().partition(head, 3)
traversal(head)

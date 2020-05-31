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
    # @return the head node in the linked list
    def reorderList(self, head):
        mid, isEven = self.findMid(head)
        lasthead = self.reverse(mid)
        res = tail = None

        def insertNode(head, tail, node):
            if tail is None:
                head = tail = node
            else:
                tail.next = node
                tail = node
            return head, tail

        turn = True
        while head and lasthead:
            if turn:
                node = ListNode(head.val)
                head = head.next
            else:
                node = ListNode(lasthead.val)
                lasthead = lasthead.next
            res, tail = insertNode(res, tail, node)
            turn = not turn
        if not isEven:
            res, tail = insertNode(res, tail, ListNode(head.val))
        return res

    def findMid(self, head):
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        isEven = True
        if fast:
            slow = slow.next
            isEven = False
        return slow, isEven

    def reverse(self, head):
        prev, next = None, head
        while next:
            nextnext = next.next
            next.next = prev
            prev = next
            next = nextnext
        return prev


head = array2list([1])
head = Solution().reorderList(head)
traversal(head)

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


class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def deleteDuplicates(self, A):
        prev, current = None, A
        while current:
            isAdded = True
            while current.next and current.next.val == current.val:
                current = current.next
                isAdded = False
            if isAdded:
                if prev:
                    prev.next = current
                else:
                    A = current
                prev = current
            current = current.next
        if not prev:
            return None
        else:
            prev.next = None
            return A


a = [1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5, 6, 7, 7, 7, 7, 8, 8, 8, 9, 9, 9,
     9, 9, 10, 10, 10, 10, 10, 10, 11, 11, 11, 11, 11, 11, 11, 12, 12, 12, 13, 13, 13, 14, 14, 14, 15, 15, 15, 15, 15,
     16, 16, 16, 16, 17, 18, 18, 19, 19, 19, 19, 19, 19, 19, 19, 20, 20, 20, 20, 20, 20, 20, 20, 20]
head = array2list(a)
res = Solution().deleteDuplicates(head)
while res:
    print(res.val, end=" ")
    res = res.next

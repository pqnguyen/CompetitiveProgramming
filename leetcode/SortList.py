# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        return self.mergeSort(head)

    def mergeSort(self, head):
        if not head or not head.next: return head
        mid = self.findMiddle(head)
        next = mid.next
        mid.next = None
        left = self.mergeSort(head)
        right = self.mergeSort(next)
        return self.merge(left, right)

    def merge(self, head1, head2):
        head = tail = ListNode(-1)
        while head1 or head2:
            node = None
            if not head1 or (head2 and head1.val > head2.val):
                node = head2
                head2 = head2.next
            elif not head2 or (head1 and head2.val >= head1.val):
                node = head1
                head1 = head1.next
            tail.next = node
            tail = node
        return head.next

    def findMiddle(self, head):
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            if not fast: break
            slow = slow.next
        return slow


head = tail = ListNode(-1)
ls = [4, 2, 1, 3]
for num in ls:
    tail.next = ListNode(num)
    tail = tail.next
Solution().sortList(head.next)

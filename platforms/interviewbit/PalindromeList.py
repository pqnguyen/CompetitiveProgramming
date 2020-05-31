# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @return an integer
    def lPalin(self, root):
        mid = self.findmid(root)
        head = self.reverse(mid)
        while head:
            if head.val != root.val: return 0
            head = head.next
            root = root.next
        return 1

    def findmid(self, root):
        slow = fast = root
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        if fast:
            slow = slow.next
        return slow

    def reverse(self, root):
        if not root or not root.next: return root
        prev, next = root, root.next
        while next:
            dupnext = next.next
            next.next = prev
            prev = next
            next = dupnext
        root.next = None
        return prev

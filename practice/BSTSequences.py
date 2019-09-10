# Cracking the coding interview - 4.9
# BST Sequences: A binary search tree was created by traversing through an array from left to right
# and inserting each element. Given a binary search tree with distinct elements, print all possible
# arrays that could have led to this tree.
from collections import deque


class TreeNode:
    def __init__(self, val):
        self.value = val
        self.left = self.right = None


class Solution:
    def all_sequences(self, root):
        if not root: return [deque()]

        results = []
        left_seq = self.all_sequences(root.left)
        right_seq = self.all_sequences(root.right)

        prefix = deque([root.value])
        for left in left_seq:
            for right in right_seq:
                self.wave_lists(left, right, results, prefix)

        return results

    def wave_lists(self, first, second, results, prefix):
        if not first or not second:
            result = prefix.copy()
            result.extend(first)
            result.extend(second)
            results.append(result)
            return

        head_first = first.popleft()
        prefix.append(head_first)
        self.wave_lists(first, second, results, prefix)
        prefix.pop()
        first.appendleft(head_first)

        head_second = second.popleft()
        prefix.append(head_second)
        self.wave_lists(first, second, results, prefix)
        prefix.pop()
        second.appendleft(head_second)


root = TreeNode(2)
one = TreeNode(1)
three = TreeNode(3)
root.left = one
root.right = three

seqs = Solution().all_sequences(root)
print(seqs)

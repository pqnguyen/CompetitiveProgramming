# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


from typing import List


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        return self.sortedArrayToBSTUtil(nums, 0, len(nums) - 1)

    def sortedArrayToBSTUtil(self, nums, begin, end):
        if begin > end: return None
        mid = (begin + end) // 2
        node = TreeNode(nums[mid])
        node.left = self.sortedArrayToBSTUtil(nums, begin, mid - 1)
        node.right = self.sortedArrayToBSTUtil(nums, mid + 1, end)
        return node

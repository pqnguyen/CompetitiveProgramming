# https://leetcode.com/problems/maximum-depth-of-n-ary-tree/
"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""


class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root: return 0
        maxDepth = 1
        for child in root.children:
            maxDepth = max(maxDepth, self.maxDepth(child) + 1)
        return maxDepth

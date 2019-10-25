# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import defaultdict


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        pathCount = defaultdict(int)
        return self.pathSumUtil(root, sum, 0, pathCount)

    def pathSumUtil(self, root, sum, runningSum, pathCount):
        if not root: return 0
        runningSum += root.val
        restSum = runningSum - sum
        count = 0
        count += pathCount[restSum]
        if runningSum == sum: count += 1
        pathCount[runningSum] += 1
        count += self.pathSumUtil(root.left, sum, runningSum, pathCount)
        count += self.pathSumUtil(root.right, sum, runningSum, pathCount)
        pathCount[runningSum] -= 1
        return count

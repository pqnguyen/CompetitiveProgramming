from typing import List


class Node:
    def __init__(self, val):
        self.val = val
        self.freq = 1
        self.leftChildren = 0
        self.left = self.right = None


class RefValue:
    def __init__(self):
        self.val = 0


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        root = None
        for i in range(n - 1, -1, -1):
            num = nums[i]
            ref = RefValue()
            root = self.insert(root, num, ref)
            res[i] = ref.val
        return res

    def insert(self, root, val, ref):
        if not root: return Node(val)
        if val > root.val:
            ref.val += root.leftChildren + root.freq
        elif val == root.val:
            ref.val += root.leftChildren

        if val == root.val:
            root.freq += 1
            return root
        if val > root.val:
            root.right = self.insert(root.right, val, ref)
        else:
            root.left = self.insert(root.left, val, ref)
            root.leftChildren += 1
        return root


nums = [1, 6, 5, 4, 3, 6, 1]
res = Solution().countSmaller(nums)
print(res)

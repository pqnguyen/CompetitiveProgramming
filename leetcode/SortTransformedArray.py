from collections import defaultdict
from typing import List


class Solution:
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int):
        for i in range(len(nums)):
            nums[i] = self.f(a, b, c, nums[i])
        self.quicksort(nums, 0, len(nums) - 1)

    def quicksort(self, nums, left, right):
        if left >= right: return
        mid = self.partition(nums, left, right)
        self.quicksort(nums, left, mid - 1)
        self.quicksort(nums, mid + 1, right)

    def partition(self, nums, left, right):
        wall = 0
        for i in range(left, right):
            if nums[i] < nums[right]:
                nums[wall], nums[i] = nums[i], nums[wall]
                wall += 1
        nums[wall], nums[right] = nums[right], nums[wall]
        return wall

    def f(self, a, b, c, x):
        return a * (x ** 2) + b * x + c


nums = [-4, -2, 2, 4]
Solution().sortTransformedArray(nums, a=1, b=3, c=5)
print(nums)

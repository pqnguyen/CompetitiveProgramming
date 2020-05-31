# https://leetcode.com/problems/sort-an-array/
from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.quicksort(nums, 0, len(nums) - 1)
        return nums

    def quicksort(self, nums, left, right):
        if left >= right: return
        mid = self.partition(nums, left, right)
        self.quicksort(nums, left, mid - 1)
        self.quicksort(nums, mid + 1, right)

    def partition(self, nums, left, right):
        wall = left
        for i in range(left, right):
            if nums[i] <= nums[right]:
                nums[wall], nums[i] = nums[i], nums[wall]
                wall += 1
        nums[wall], nums[right] = nums[right], nums[wall]
        return wall


res = Solution().sortArray([5, 2, 3, 1])
print(res)

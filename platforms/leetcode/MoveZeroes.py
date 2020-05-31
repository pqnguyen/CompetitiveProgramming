# https://leetcode.com/problems/move-zeroes/
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        wall = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[wall], nums[i] = nums[i], nums[wall]
                wall += 1
        return nums

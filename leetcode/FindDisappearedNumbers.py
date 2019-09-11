# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/
from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            index = abs(nums[i]) - 1
            if nums[index] > 0:
                nums[index] *= -1
        res = []
        for i in range(len(nums)):
            if nums[i] > 0:
                res.append(i + 1)
        return res

    def findDisappearedNumbers2(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        for i in range(n):
            nums[nums[i] % (n + 1) - 1] += (n + 1)

        res = []
        for i in range(n):
            if nums[i] // (n + 1) == 0:
                res.append(i + 1)

        return res
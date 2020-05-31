# https://leetcode.com/problems/majority-element/
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res, count = -1, 0
        for i in range(len(nums)):
            if not count: res = nums[i]
            if nums[i] == res:
                count += 1
            else:
                count -= 1
        return res

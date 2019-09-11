# https://leetcode.com/problems/maximum-subarray/
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums: return 0
        res = nums[0]
        total = 0
        for i in range(len(nums)):
            total = max(total + nums[i], nums[i])
            res = max(res, total)
        return res

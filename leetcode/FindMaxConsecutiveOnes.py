# https://leetcode.com/problems/max-consecutive-ones/
from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = 0
        consecutive = 0
        for i in range(len(nums)):
            consecutive += 1
            if nums[i] == 0:
                consecutive = 0
            res = max(res, consecutive)
        return res

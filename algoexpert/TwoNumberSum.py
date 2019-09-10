from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = {}
        for idx, e in enumerate(nums):
            remainder = target - e
            if remainder in m:
                return [m[remainder], idx]
            m[e] = idx

        return []

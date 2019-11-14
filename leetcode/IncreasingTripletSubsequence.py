from bisect import bisect_left as lower_bound
from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        increasing = [0] * len(nums)
        length = 0
        for i, num in enumerate(nums):
            index = lower_bound(increasing, num, 0, length)
            if index == length: length += 1
            if length >= 3: return True
            increasing[index] = num
        return False


print(Solution().increasingTriplet([5, 4, 3, 2, 1]))

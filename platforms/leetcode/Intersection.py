# https://leetcode.com/problems/intersection-of-two-arrays/
from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        snums1 = set(num for num in nums1)
        res = set(num for num in nums2 if num in snums1)
        return list(res)

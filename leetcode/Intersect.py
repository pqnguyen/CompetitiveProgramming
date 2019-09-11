# https://leetcode.com/problems/intersection-of-two-arrays-ii/
from collections import defaultdict
from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        tnums1 = self.frequency(nums1)
        tnums2 = self.frequency(nums2)
        res = []
        for num, f in tnums1.items():
            res.extend([num] * min(f, tnums2[num]))
        return res

    def frequency(self, nums):
        t = defaultdict(int)
        for num in nums:
            t[num] += 1
        return t

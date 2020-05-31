# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        begin, end = 0, len(numbers) - 1
        while begin < end:
            s = numbers[begin] + numbers[end]
            if s == target:
                return [begin + 1, end + 1]
            elif s > target:
                end -= 1
            else:
                begin += 1
        return [0, 0]

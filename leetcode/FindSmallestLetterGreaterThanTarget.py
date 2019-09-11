# https://leetcode.com/problems/find-smallest-letter-greater-than-target/
from typing import List


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        first, last = 0, len(letters) - 1
        res = 0
        while first <= last:
            mid = (first + last) // 2
            if letters[mid] > target:
                last = mid - 1
                res = mid
            else:
                first = mid + 1
        return letters[res]


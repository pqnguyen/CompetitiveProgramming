# https://leetcode.com/problems/smallest-range-i/
class Solution:
    def smallestRangeI(self, A: List[int], K: int) -> int:
        mi, mx = min(A), max(A)
        if mi + K >= mx or mi + K >= mx - K:
            return 0
        else:
            return mx - K - K - mi

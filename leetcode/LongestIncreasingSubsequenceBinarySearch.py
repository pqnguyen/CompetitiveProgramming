from bisect import bisect_left as lower_bound
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        a = [0] * n
        length = 0
        for i in range(n):
            idx = lower_bound(a, nums[i], 0, length)
            if idx >= length: length += 1
            a[idx] = nums[i]

        return length

    def lower_bound(self, a, start, end, key):
        res = end + 1
        while start <= end:
            mid = (start + end) // 2
            if a[mid] >= key:
                res = mid
                end = mid - 1
            else:
                start = mid + 1
        return res


res = Solution().lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18])
print(res)

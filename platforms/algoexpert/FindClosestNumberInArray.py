from typing import List


class Solution:
    def findClosetNumberInArray(self, nums: List[int], target: int):
        sorted(nums)
        idx = self.lowerBound(nums, target)
        if idx == -1:
            return nums[0]
        else:
            res = nums[idx]
            if idx + 1 < len(nums):
                if abs(target - res) > abs(target - nums[idx + 1]):
                    res = nums[idx + 1]
            return res

    def lowerBound(self, nums, target):
        res = -1
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] <= target:
                res = mid
                lo = mid + 1
            else:
                hi = mid - 1

        return res


sol = Solution()
print(sol.findClosetNumberInArray([1, 2, 4, 5, 6, 6, 8, 9, 12, 13, 14], 11))

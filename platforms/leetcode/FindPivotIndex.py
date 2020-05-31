# https://leetcode.com/problems/find-pivot-index/
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        left = 0
        for i in range(len(nums)):
            if i >= 1:
                left += nums[i - 1]

            if left == total - left - nums[i]:
                return i
        return -1

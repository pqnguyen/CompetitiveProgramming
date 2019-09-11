# https://leetcode.com/problems/longest-continuous-increasing-subsequence/
class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if not nums: return 0
        res = count = 1
        for i in range(1, len(nums)):
            count += 1
            if nums[i] <= nums[i - 1]:
                count = 1
            res = max(res, count)
        return res


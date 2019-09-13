# https://leetcode.com/problems/remove-duplicates-from-sorted-array/
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        wall = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[wall]:
                nums[wall + 1] = nums[i]
                wall += 1
        return wall + 1


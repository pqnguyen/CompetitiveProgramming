# https://leetcode.com/explore/learn/card/array-and-string/205/array-two-pointer-technique/1151/
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        wall = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[i], nums[wall] = nums[wall], nums[i]
                wall += 1
        return wall

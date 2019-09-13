# https://leetcode.com/problems/rotate-array/
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        nums.reverse()
        self.reverse(nums, 0, k)
        self.reverse(nums, k, len(nums))

    def reverse(self, nums, begin, end):
        while begin < end:
            nums[begin], nums[end - 1] = nums[end - 1], nums[begin]
            begin += 1
            end -= 1

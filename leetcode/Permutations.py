from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.permuteUtil(nums, 0, res)
        return res

    def permuteUtil(self, nums, index, res):
        if index == len(nums):
            res.append(nums[:])
            return
        for i in range(index, len(nums)):
            nums[i], nums[index] = nums[index], nums[i]
            self.permuteUtil(nums, index + 1, res)
            nums[i], nums[index] = nums[index], nums[i]


res = Solution().permute([1, 2, 3])
print(res)

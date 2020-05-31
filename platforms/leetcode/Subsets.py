from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.subsetsUtil(nums, 0, [], res)
        return res

    def subsetsUtil(self, nums, index, subset, res):
        if index == len(nums):
            res.append(subset[:])
            return

        for choose in [True, False]:
            if choose: subset.append(nums[index])
            self.subsetsUtil(nums, index + 1, subset, res)
            if choose: subset.pop()


res = Solution().subsets([1, 2, 3])
print(res)

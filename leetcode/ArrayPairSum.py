from typing import List


class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        total = 0
        for i in range(0, len(nums), 2):
            print(nums[i])
            total += nums[i]
        return total


print(Solution().arrayPairSum([1, 4, 3, 2]))

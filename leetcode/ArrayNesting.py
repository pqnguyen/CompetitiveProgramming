from typing import List


class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n
        for index, num in enumerate(nums):
            if not dp[index]:
                self.dfs(nums, index, dp)
        return max(dp) - 1

    def dfs(self, nums, index, dp):
        dp[index] = 1
        if not dp[nums[index]]:
            dp[index] += self.dfs(nums, nums[index], dp)
        else:
            dp[index] += dp[nums[index]]
        return dp[index]


res = Solution().arrayNesting([1, 2, 3, 4, 5, 0])
print(res)

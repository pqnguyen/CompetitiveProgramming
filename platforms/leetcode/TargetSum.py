class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        dp = {}
        return self.findTargetSumWaysUtil(nums, 0, S, dp)

    def findTargetSumWaysUtil(self, nums, index, S, dp):
        if index == len(nums):
            if S == 0: return 1
            return 0

        if (index, S) in dp: return dp[index, S]
        ways = 0
        for sign in [1, -1]:
            ways += self.findTargetSumWaysUtil(nums, index + 1, S - nums[index] * sign, dp)
        dp[index, S] = ways
        return ways
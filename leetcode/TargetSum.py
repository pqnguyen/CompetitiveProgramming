# https://leetcode.com/explore/learn/card/queue-stack/232/practical-application-stack/1389/
from collections import defaultdict
from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        m = defaultdict(dict)
        ways = self.dfs(nums, 0, S, m)
        return ways

    def dfs(self, nums, index, S, m):
        if index == len(nums):
            if S == 0:
                return 1
            else:
                return 0
        ways = 0
        if S in m[index]: return m[index][S]
        for sign in [1, -1]:
            s = S - nums[index] * sign
            ways += self.dfs(nums, index + 1, s, m)
        m[index][S] = ways
        return ways


res = Solution().findTargetSumWays([29, 6, 7, 36, 30, 28, 35, 48, 20, 44, 40, 2, 31, 25, 6, 41, 33, 4, 35, 38], 35)
print(res)

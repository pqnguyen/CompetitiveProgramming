# https://leetcode.com/explore/learn/card/array-and-string/205/array-two-pointer-technique/1299/
MAX_INT = 2 ** 31 - 1

class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        current = index = 0
        res = MAX_INT
        for i in range(len(nums)):
            current += nums[i]
            while current >= s and index <= i:
                res = min(res, i - index + 1)
                current -= nums[index]
                index += 1
        return res if res != MAX_INT else 0

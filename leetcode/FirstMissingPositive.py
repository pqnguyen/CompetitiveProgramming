class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if 1 not in nums: return 1
        n = len(nums)
        for i in range(n):
            if nums[i] <= 0 or nums[i] > n:
                nums[i] = 1
        for i in range(n):
            num = abs(nums[i]) % n
            nums[num] = -abs(nums[num])
        for i in range(1, n):
            if nums[i] > 0: return i
        if nums[0] > 0: return n
        return n + 1
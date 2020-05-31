# https://leetcode.com/problems/contains-duplicate-ii/
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        unique = set()
        for i in range(len(nums)):
            if i > k: unique.remove(nums[i - k - 1])
            if nums[i] in unique: return True
            unique.add(nums[i])
        return False

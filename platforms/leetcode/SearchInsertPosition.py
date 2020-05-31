# https://leetcode.com/problems/search-insert-position/
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        first, last = 0, len(nums) - 1
        res = -1
        while first <= last:
            mid = (first + last) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                first = mid + 1
                res = mid
            else:
                last = mid - 1
        return res + 1

# https://leetcode.com/problems/third-maximum-number/
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        thirdNums = set()
        for num in nums:
            if len(thirdNums) < 3:
                thirdNums.add(num)
            elif num not in thirdNums:
                minimum = min(thirdNums)
                if num > minimum:
                    thirdNums.remove(minimum)
                    thirdNums.add(num)
        return min(thirdNums) if len(thirdNums) == 3 else max(thirdNums)
# https://leetcode.com/problems/height-checker/
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sortedHeights = sorted(heights)
        res = 0
        for i in range(len(heights)):
            if sortedHeights[i] ^ heights[i]:
                res += 1
        return res
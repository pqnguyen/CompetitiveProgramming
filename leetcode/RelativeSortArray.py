# https://leetcode.com/problems/relative-sort-array/
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        f = [0] * 1001
        for num in arr1: f[num] += 1
        res = []
        for num in arr2:
            res.extend([num] * f[num])
            f[num] = 0
        for i in range(len(f)):
            if f[i]:
                res.extend([i] * f[i])
        return res

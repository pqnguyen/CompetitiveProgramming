from collections import Counter
from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        table = Counter(nums)
        self.permuteUniqueHelper(table, n, [], res)
        return res

    def permuteUniqueHelper(self, table, n, current, res):
        if len(current) == n:
            res.append(current[:])
            return

        for num in table.keys():
            if table[num]:
                table[num] -= 1
                current.append(num)
                self.permuteUniqueHelper(table, n, current, res)
                current.pop()
                table[num] += 1


res = Solution().permuteUnique([1, 1, 1, 2])
print(res)

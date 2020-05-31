from collections import defaultdict
from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        m = defaultdict(list)
        exists = set()
        n = len(nums)
        res = []
        for i in range(n - 1):
            for j in range(i + 1, n):
                total = nums[i] + nums[j]
                for pairI, pairJ in m[target - total]:
                    if i != pairI and i != pairJ and j != pairI and j != pairJ:
                        quadruplets = sorted([nums[i], nums[j], nums[pairI], nums[pairJ]])
                        key = "{}:{}:{}:{}".format(*quadruplets)
                        if key not in exists:
                            exists.add(key)
                            res.append(quadruplets)
                m[total].append([i, j])
        return res


res = Solution().fourSum([1, 0, -1, 0, -2, 2], 0)
print(res)

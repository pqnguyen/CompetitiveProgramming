from typing import List

MAX_INT = 2 ** 31 - 1


class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        if not houses: return 0
        houses.sort()
        heaters.sort()
        heaters.append(MAX_INT)
        res = index = i = 0
        while index < len(houses):
            a = abs(heaters[i] - houses[index])
            b = abs(heaters[i + 1] - houses[index])
            if b <= a:
                i += 1
            else:
                res = max(res, a)
                index += 1
        return res


res = Solution().findRadius([1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 4, 4, 5, 6])
print(res)

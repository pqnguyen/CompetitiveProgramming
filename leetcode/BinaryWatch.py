from typing import List


class Solution:
    def readBinaryWatch(self, num: int) -> List[str]:
        res = []
        for h in range(12):
            for m in range(60):
                if self.countBit(h) + self.countBit(m) == num:
                    res.append(self.representTime(h, m))
        return res

    def representTime(self, h, m):
        return "{}:{:02d}".format(h, m)

    def countBit(self, n):
        count = 0
        while n:
            if n & 1 == 1: count += 1
            n = n >> 1
        return count


res = Solution().readBinaryWatch(1)
print(res)

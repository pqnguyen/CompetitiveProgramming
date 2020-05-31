from collections import defaultdict
from typing import List


class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        freq = self.frequency(A[0])
        for i in range(len(A)):
            s = A[i]
            current = self.frequency(s)
            for ch, f in freq.items():
                freq[ch] = min(f, current[ch])

        res = []
        for ch, f in freq.items():
            if f:
                res.extend([ch] * f)
        return res

    def frequency(self, s):
        f = defaultdict(int)
        for ch in s: f[ch] += 1
        return f


res = Solution().commonChars(["cool", "lock", "cook"])
print(res)

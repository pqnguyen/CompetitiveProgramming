from collections import Counter, defaultdict
from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        counterP = Counter(p)
        counter = defaultdict(int)

        cnt = 0
        start = 0
        res = []
        for i, ch in enumerate(s):
            if ch not in counterP:
                counter, cnt = defaultdict(int), 0
                start = i + 1
                continue

            while counter[ch] == counterP[ch]:
                counter[s[start]] -= 1
                if counter[s[start]] < counterP[s[start]]: cnt -= 1
                start += 1

            counter[ch] += 1
            if counter[ch] == counterP[ch]: cnt += 1
            if cnt == len(counterP):
                res.append(start)
                counter[s[start]] -= 1
                start += 1
                cnt -= 1
        return res


s = ""
p = "a"
res = Solution().findAnagrams(s, p)
print(res)

from collections import defaultdict


class Solution:
    def LSAtMost2DistinctCharacters(self, str):
        count = 0
        start = res = 0
        tb = defaultdict(int)
        for i in range(len(str)):
            ch = str[i]
            if tb[ch] == 0:
                count += 1
                tb[ch] += 1

            while start < i and count > 2:
                tb[str[start]] -= 1
                if tb[str[start]] == 0:
                    count -= 1
                start += 1

            res = max(res, i - start + 1)

        return res


res = Solution().LSAtMost2DistinctCharacters("eceba")
print(res)

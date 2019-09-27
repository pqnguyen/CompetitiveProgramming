from collections import defaultdict


class Solution:
    def LSAtMostKDistinctCharacters(self, str, k):
        count = 0
        start = res = 0
        tb = defaultdict(int)
        for i in range(len(str)):
            ch = str[i]
            if tb[ch] == 0:
                count += 1
                tb[ch] += 1

            while start <= i and count > k:
                tb[str[start]] -= 1
                if tb[str[start]] == 0:
                    count -= 1
                start += 1

            res = max(res, i - start + 1)

        return res


res = Solution().LSAtMostKDistinctCharacters("eceba", 6)
print(res)

from collections import defaultdict


class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        res = 0
        for unique in range(1, 27):
            length = self.helper(s, k, unique)
            res = max(res, length)
        return res

    def helper(self, s, k, uniqueTarget):
        table = defaultdict(int)
        unique = 0
        uniqueWithNoLessK = 0
        begin = end = 0
        d = 0
        while end < len(s):
            table[s[end]] += 1
            if table[s[end]] == 1: unique += 1
            if table[s[end]] == k: uniqueWithNoLessK += 1
            end += 1

            while unique > uniqueTarget:
                if table[s[begin]] == 1: unique -= 1
                if table[s[begin]] == k: uniqueWithNoLessK -= 1
                table[s[begin]] -= 1
                begin += 1

            if unique == uniqueTarget and unique == uniqueWithNoLessK:
                d = max(d, end - begin)

        return d


res = Solution().longestSubstring("ababbc", 2)
print(res)

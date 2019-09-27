from collections import defaultdict


class Solution:
    def groupStrings(self, ls):
        tb = defaultdict(list)
        for str in ls:
            key = self.getBitMap(str)
            tb[key].append(str)

        return list(tb.values())

    def getBitMap(self, s):
        a = [0] * len(s)
        for i in range(1, len(s)):
            a[i] = (ord(s[i]) - ord(s[0])) + 26 if ord(s[i]) - ord(s[0]) < 0 else ord(s[i]) - ord(s[0])
        return "".join(str(diff) for diff in a)


ls = ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"]
res = Solution().groupStrings(ls)
print(res)

class Solution:
    mapping = {0: 0, 1: 1, 6: 9, 9: 6, 8: 8}

    def generateStrobogrammatic(self, n):
        res = []
        if n < 1: return res
        chs = [0] * n
        self.helper(chs, 0, n - 1, res)
        return res

    def helper(self, chs, lo, hi, res):
        if lo > hi:
            if len(chs) == 1 or chs[0] != 0:
                res.append("".join(str(ch) for ch in chs))
            return

        for a, b in self.mapping.items():
            if lo == hi and a != b: continue
            chs[lo] = a
            chs[hi] = b
            self.helper(chs, lo + 1, hi - 1, res)


res = Solution().generateStrobogrammatic(3)
print(res)

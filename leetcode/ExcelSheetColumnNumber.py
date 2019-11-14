class Solution:
    def titleToNumber(self, s: str) -> int:
        res = 0
        for ch in s:
            res = res * 26 + (ord(ch) - ord('A') + 1)
        return res


print(Solution().titleToNumber("ZY"))

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        res = count = 0
        for i, ch in enumerate(s):
            if ch == 'R':
                count -= 1
            else:
                count += 1
            if count == 0:
                res += 1
                count = 0
        return res


res = Solution().balancedStringSplit("LLR")
print(res)

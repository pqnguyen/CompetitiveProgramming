# https://leetcode.com/problems/long-pressed-name/
class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i = j = 0
        n, m = len(name), len(typed)
        while i < n and j < m:
            ci = cj = 1
            while i + 1 < n and name[i] == name[i + 1]:
                i += 1
                ci += 1
            while j + 1 < m and typed[j] == typed[j + 1]:
                j += 1
                cj += 1
            if name[i] != typed[j] or ci > cj:
                return False
            i += 1
            j += 1
        return i == n and j == m


res = Solution().isLongPressedName("laidenz", "laidenn")
print(res)

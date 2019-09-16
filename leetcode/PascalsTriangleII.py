# https://leetcode.com/explore/learn/card/array-and-string/204/conclusion/1171/
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        prev = [1]
        for i in range(1, rowIndex + 1):
            next = [1] * (i + 1)
            for j in range(1, len(next) - 1):
                next[j] = prev[j - 1] + prev[j]
            prev = next
        return prev

from collections import defaultdict
from typing import List


class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        table = defaultdict(list)
        for word in words:
            for trans in self.transformRemove(word):
                table[trans].append(word)

        dp = defaultdict(int)
        for word in words:
            if not dp[word]:
                self.dfs(table, word, dp)

        return max(dp.values())

    def dfs(self, table, word, dp):
        if dp[word]: return dp[word]
        dp[word] = 1
        for trans in self.transformInsert(word):
            for originalWord in table[trans]:
                length = self.dfs(table, originalWord, dp)
                dp[word] = max(dp[word], 1 + length)
        return dp[word]

    def transformRemove(self, word):
        res = []
        for i in range(len(word)):
            s = word[:i] + "_" + word[i + 1:]
            res.append(s)
        return res

    def transformInsert(self, word):
        res = []
        for i in range(len(word) + 1):
            s = word[:i] + "_" + word[i:]
            res.append(s)
        return res


words = ["a", "b", "ba", "bca", "bda", "bdca"]
res = Solution().longestStrChain(words)
print(res)

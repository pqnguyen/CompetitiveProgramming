from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}
        breakable = self.wordBreakHelper(s, 0, wordDict, memo)
        return breakable

    def wordBreakHelper(self, s, index, words, memo):
        if index == len(s): return True

        if index in memo: return memo[index]
        for word in words:
            if s.startswith(word, index):
                startindex = index + len(word)
                if self.wordBreakHelper(s, startindex, words, memo):
                    memo[index] = True
                    return True
        memo[index] = False
        return False


s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]
print(Solution().wordBreak(s, wordDict))

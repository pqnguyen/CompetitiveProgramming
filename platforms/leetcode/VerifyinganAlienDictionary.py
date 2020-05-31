# https://leetcode.com/problems/verifying-an-alien-dictionary/
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        a = {ch: index for index, ch in enumerate(order)}
        for i in range(1, len(words)):
            if not self.compareWord(words[i - 1], words[i], a):
                return False
        return True

    def compareWord(self, word1, word2, a):
        n, m = len(word1), len(word2)
        for i in range(min(n, m)):
            if word1[i] == word2[i]:
                continue
            return a[word1[i]] < a[word2[i]]
        return n <= m

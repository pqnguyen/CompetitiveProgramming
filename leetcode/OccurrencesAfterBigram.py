# https://leetcode.com/problems/occurrences-after-bigram/
class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        pattern = first + ' ' + second
        words = text.split()
        res = []
        for i in range(1, len(words) - 1):
            if words[i - 1] + ' ' + words[i] == pattern:
                res.append(words[i + 1])
        return res

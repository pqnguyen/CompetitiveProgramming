# https://leetcode.com/problems/uncommon-words-from-two-sentences/
class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        fa = self.counter(A)
        fb = self.counter(B)
        res = []
        for key, f in fa.items():
            if f == 1 and key not in fb:
                res.append(key)

        for key, f in fb.items():
            if f == 1 and key not in fa:
                res.append(key)
        return res

    def counter(self, s):
        f = collections.defaultdict(int)
        for word in s.split():
            f[word] += 1
        return f

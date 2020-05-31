# https://leetcode.com/problems/x-of-a-kind-in-a-deck-of-cards/
class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        counter = collections.defaultdict(int)
        for ele in deck: counter[ele] += 1
        x = 0
        for key, c in counter.items():
            x = self.gcd(x, c)
        return x >= 2

    def gcd(self, a, b):
        if a == 0: return b
        return self.gcd(b % a, a)

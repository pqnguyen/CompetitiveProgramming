# https://leetcode.com/problems/reverse-only-letters/
class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        S = list(S)
        first, last = 0, len(S) - 1
        while first < last:
            while first < len(S) and not S[first].isalpha(): first += 1
            while last >= 0 and not S[last].isalpha(): last -= 1
            if first < last:
                S[first], S[last] = S[last], S[first]
                first += 1
                last -= 1
        return "".join(S)
from collections import Counter, defaultdict


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        counterT = Counter(t)
        counterWindow = defaultdict(int)
        count = 0
        start = end = 0
        mxStart, mxEnd = 0, len(s) + 1
        while end <= len(s):
            if count < len(counterT.keys()):
                if end == len(s): break
                ch = s[end]
                counterWindow[ch] += 1
                if ch in counterT and counterWindow[ch] == counterT[ch]:
                    count += 1
                end += 1
            else:
                if end - start < mxEnd - mxStart:
                    mxStart = start
                    mxEnd = end
                ch = s[start]
                counterWindow[ch] -= 1
                if ch in counterT and counterWindow[ch] < counterT[ch]:
                    count -= 1
                start += 1

        if mxEnd == len(s) + 1: return ""
        return s[mxStart: mxEnd]


s = "ADOBECODEBANC"
t = "C"
res = Solution().minWindow(s, t)
print(res)

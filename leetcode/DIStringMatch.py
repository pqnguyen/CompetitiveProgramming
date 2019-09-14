# https://leetcode.com/problems/di-string-match/
class Solution:
    def diStringMatch(self, S: str) -> List[int]:
        res = [i for i in range(len(S) + 1)]

        for i in range(len(S)):
            if S[i] == 'D':
                for j in range(i, -1, -1):
                    if S[j] == 'D':
                        res[j], res[j + 1] = res[j + 1], res[j]
                    else:
                        break
        return res

    def diStringMatchBetter(self, S):
        lo, hi = 0, len(S)
        ans = []
        for x in S:
            if x == 'I':
                ans.append(lo)
                lo += 1
            else:
                ans.append(hi)
                hi -= 1

        return ans + [lo]

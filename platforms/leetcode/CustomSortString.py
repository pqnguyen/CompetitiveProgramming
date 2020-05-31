from collections import Counter


class Solution:
    def customSortString(self, S: str, T: str) -> str:
        counterT = Counter(T)
        left = ""
        for ch in S:
            if ch in counterT:
                left += ch * counterT[ch]
            counterT[ch] = 0
        right = "".join([key * count for key, count in counterT.items() if count > 0])
        return left + right


S = "cba"
T = "abcd"
res = Solution().customSortString(S, T)
print(res)

from collections import Counter, defaultdict


class Solution:
    # @param A : string
    # @param B : string
    # @return a strings
    def minWindow(self, s, pattern):
        if not s or not pattern: return ""
        counterPattern = Counter(pattern)
        counter = defaultdict(int)
        left = right = 0
        start, end = 0, len(s) + 1
        count = 0
        while right < len(s):
            counter[s[right]] += 1
            if s[right] in counterPattern and counter[s[right]] <= counterPattern[s[right]]:
                count += 1

            while count == len(pattern):
                if right - left < end - start:
                    start, end = left, right
                counter[s[left]] -= 1
                if s[left] in counterPattern and counter[s[left]] < counterPattern[s[left]]:
                    count -= 1
                left += 1
            right += 1

        if end == len(s) + 1: return ""
        return s[start:end + 1]


S = "AAAAA"
T = "A"
res = Solution().minWindow(S, T)
print(res)

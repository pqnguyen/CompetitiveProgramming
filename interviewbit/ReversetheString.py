class Solution:
    # @param s : string
    # @return a strings
    def solve(self, s):
        s = list(s)
        self.reverse(s, 0, len(s) - 1)
        start = 0
        for i in range(len(s)):
            if s[i] == ' ':
                if s[start] != ' ': self.reverse(s, start, i - 1)
                start = i + 1
        self.reverse(s, start, len(s) - 1)
        return "".join(s)

    def reverse(self, s, start, end):
        while start < end:
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1


res = Solution().solve("   the sky is blue   e")
print(res)
